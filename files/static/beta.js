/* OUTLINE

8 --> workout.html
39 --> betaone.html

*/

// workout.html

document.getElementById("testbox1").addEventListener("click", unlockTwo);

function unlockTwo() {
	if (document.getElementById("testbox1").checked = true) {
		document.getElementById("testbox2").disabled = false;
	}
}

document.getElementById("testbox2").addEventListener("click", unlockThree);

function unlockThree() {
	if (document.getElementById("testbox2").checked = true) {
		document.getElementById("testbox3").disabled = false;
	} else if (document.getElementById("testbox2").checked = false) {
		document.getElementById("testbox3").disabled = true;
	}
}

document.getElementById("testbox3").addEventListener("click", showFinish);

function showFinish() {
  var d = document.getElementById("finisher");
  if (d.style.display === "block") {
	d.style.display = "none";
  } else {
  	d.style.display = "block";
  }
}

// betaone.html

document.getElementById("lol").addEventListener("click", showHide);

function showHide() {
   var x = document.getElementById("testhide");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}

function addStreak() {
    document.getElementById("streak").value++;
}

function subtractStreak() {
	document.getElementById("streak").value--;
}

function addTotal() {
	document.getElementById("total").value++;
}

function subtractTotal() {
	document.getElementById("total").value--;
}