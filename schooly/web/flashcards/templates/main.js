// TODO(you): Modify the file in whatever ways necessary to implement
// the flashcard app behavior.
const app = new App();

let origin = [null,null]; //represents original position
let change = [0,0]; //represents the new position
let translate = [0,0];
let totalTranslate = [0,0];
let dragging = false;
var id;
let rotateAngle = 0;


// Drags

function startDrag(event) {
  origin[0] = event.clientX; // initial positions, ensures it will reset with movement
  origin[1] = event.clientY;
  console.log("X "+origin[0]);
  console.log("Y "+origin[1]);

  dragging = true; // starting to drag
  event.currentTarget.setPointerCapture(event.pointerId);
  clearInterval(id); // clears interval
}

function drag(event) {
  if (!dragging) {
    return;
  }
  event.preventDefault();
  translate[0] = change[0] + event.clientX - origin[0]; // How much to move
  translate[1] = change[1] + event.clientY - origin[1]; // How much to move
  totalTranslate[0] += translate[0];
  totalTranslate[1] += translate[1];
  event.currentTarget.style.transform = 'translate(' +  translate[0] + 'px,' +  translate[1] + 'px) ' ; // translates
  rotateAngle = 0.2*(event.clientX - origin[0]);
  event.currentTarget.style.transform += 'rotate(' + rotateAngle + 'deg)'; //rotates ***NOT WORKING***
  // if dragged far, changes background
  if (event.clientX - origin[0] > 150||event.clientX - origin[0] < -150) {
  	document.body.style.backgroundColor = '#97b7b7';
  } else {
  	document.body.style.backgroundColor = '#d0e6df';
  }

}

function endDrag(event) {
	dragging = false; // end of drag
	if (event.clientX - origin[0] > 150||event.clientX - origin[0] < -150){
    let ans;
		totalCard ++;
	  if (event.clientX - origin[0] > 150){
			ans = document.querySelector(".correct");
      console.log("correct");
	  } else if (event.clientX - origin[0] < -150) {
	  	ans = document.querySelector(".incorrect");
	  	wrongCards.push([app.flashcards.cardValues[0][totalCard-1],app.flashcards.cardValues[1][totalCard-1]]);
		}
		let ansNum = ans.textContent;
		ans.textContent=Number(ansNum)+1;
		if (totalCard === app.flashcards.cardValues[0].length) {
			app.flashcards.hide();
			app.results.show(Number(document.querySelector(".correct").textContent), Number(document.querySelector(".incorrect").textContent));

		} else {
			app.flashcards.show();
		}

  } else { //card pops back to the middle if less than 150 px drag
    //how much we moved
    console.log("less than 150px move");
    let backX = translate[0]*-1; //NOT WORKING RIGHT NOW
    let backY = translate[1]*-1;
    let backAngle = rotateAngle*-1;
    event.currentTarget.style.transform = "translate(0px,0px)"; //translate the opposite of what we did
    console.log("X moved back by: "+backX);
    console.log("Y moved back by: "+backY);
    event.currentTarget.style.transform += 'rotate(0 deg)'; //rotate the opposite of what we did
    console.log("Rotated back by:"+backAngle+"degrees");
  }

}