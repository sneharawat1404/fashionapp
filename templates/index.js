let textdata = ["Choose your Type Below<3", "Your Fashion OG!"];

let ref = document.getElementById("text");
let cur = document.querySelector(".cursor");
let ind = 0;
let cInd = 0;
let remove = false;

function textTypeFunction() {
  if (ind < textdata.length) {
    let currentText = textdata[ind];
    if (!remove && cInd < currentText.length) {
      ref.textContent += currentText.charAt(cInd);
      cInd++;
      setTimeout(textTypeFunction, 100);
    } else if (remove && cInd >= 0) {
      ref.textContent = currentText.substring(0, cInd);
      cInd--;
      setTimeout(textTypeFunction, 100);
    } else {
      remove = !remove;
      if (!remove) {
        ind++;
        if (ind >= textdata.length) {
          ind = 0;
        }
      }
      setTimeout(textTypeFunction, 1000);
    }
  }
}

textTypeFunction();
