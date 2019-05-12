// TODO(you): Modify the class in whatever ways necessary to implement
// the flashcard app behavior.
//
// You may need to do things such as:
// - Changing the constructor parameters
// - Adding methods
// - Adding additional fields

class Flashcard {
    constructor(containerElement, frontText, backText) {
      this.containerElement = containerElement;
  
      this._flipCard = this._flipCard.bind(this);
  
      this.flashcardElement = this._createFlashcardDOM(frontText, backText);
      this.containerElement.append(this.flashcardElement);
  
      this.flashcardElement.addEventListener('pointerup', this._flipCard);
    }
  
    // Creates the DOM object representing a flashcard with the given
    // |frontText| and |backText| strings to display on the front and
    // back of the card. Returns a reference to root of this DOM
    // snippet. Does not attach this to the page.
    //
    // More specifically, this creates the following HTML snippet in JS
    // as a DOM object:
    // <div class="flashcard-box show-word">
    //   <div class="flashcard word">frontText</div>
    //   <div class="flashcard definition">backText</div>
    // </div>
    // and returns a reference to the root of that snippet, i.e. the
    // <div class="flashcard-box">
    _createFlashcardDOM(frontText, backText) {
      const cardContainer = document.createElement('div');
      cardContainer.classList.add('flashcard-box');
      cardContainer.classList.add('show-word');
  
      //drag event listeners
      cardContainer.addEventListener('pointerdown', startDrag);
      cardContainer.addEventListener('pointermove', drag);
      cardContainer.addEventListener('pointerup', endDrag);
      
      const wordSide = document.createElement('div');
      wordSide.classList.add('flashcard');
      wordSide.classList.add('word');
      wordSide.textContent = frontText;
  
      const definitionSide = document.createElement('div');
      definitionSide.classList.add('flashcard');
      definitionSide.classList.add('definition');
      definitionSide.textContent= backText;
  
      cardContainer.appendChild(wordSide);
      cardContainer.appendChild(definitionSide);
      return cardContainer;
    }
  
    _flipCard(event) {
      this.flashcardElement.classList.toggle('show-word');
    }
  }