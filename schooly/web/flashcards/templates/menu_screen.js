// TODO(you): Modify the class in whatever ways necessary to implement
// the flashcard app behavior.
//
// You may need to do things such as:
// - Changing the constructor parameters
// - Adding methods
// - Adding additional fields

class MenuScreen {
    constructor(containerElement) {
      this.containerElement = containerElement;
  
      //adding the relevant flashcard choices
      //add the menu choices in a for loop and append the choices container
      for(let i = 0; i < FLASHCARD_DECKS.length; i++){ //rn the length should b 3
        let choice = document.createElement('div'); //create the div
        choice.className = "menu-buttons";
        let insidemap = FLASHCARD_DECKS[i]; //fetch the map inside my array
        choice.appendChild(document.createTextNode(insidemap.title)); //create the text
        choice.addEventListener('click', function() {
          app.flashcards.makeCards(i); //fill my cards
          app.menu.hide(); //hide the choices now
          app.flashcards.show(); //show flashcards you chose now
  
        }, false);
        document.getElementById("choices").appendChild(choice);
      }
    }
  
    show() {
      this.containerElement.classList.remove('inactive');
    }
  
    hide() {
      this.containerElement.classList.add('inactive');
    }
  }