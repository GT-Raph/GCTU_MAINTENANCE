//Project description: Bluecrest Student Complaint form
//Developer: Chris C. Karpee, BScIT, Semester 2
//Email: chris@foreverabc.com

function goStepTwo() {
  checkName();
  checkNum();
  Achieve();
}

function backStepOne() {
  stepInfo.style.display = "flex";
  stepPlan.style.display = "none";
  circle1.style.color = "black";
  circle1.style.backgroundColor = "rgba(255, 255, 255)";
  circle2.style.backgroundColor = "rgb(255, 255, 255, 0)";
  circle2.style.color = "white";
}

//Yes function
function yesFunc(){
    var inputContainer=document.getElementById('numSub');
    if(inputContainer.style.display=='none'){
        inputContainer.style.display='block';
    }else{inputContainer.style.display='none'
}
}

//Step three -finalcheck 

function goStepThree() {
  console.log(typeof document.getElementById("totalPrice").innerHTML);

  checkPlan();
}
function backSteptTwo() {
  stepPlan.style.display = "flex";
  stepAddOn.style.display = "none";
  circle2.style.color = "black";
  circle2.style.backgroundColor = "rgba(255, 255, 255)";
  circle3.style.backgroundColor = "rgb(255, 255, 255, 0)";
  circle3.style.color = "white";
}

function goStepFour() {
  stepSummary.style.display = "flex";
  stepAddOn.style.display = "none";
  circle3.style.color = "white";
  circle3.style.backgroundColor = "rgba(255, 255, 255, 0)";
  circle4.style.backgroundColor = "rgb(255, 255, 255)";
  circle4.style.color = "black";

  const adOnnPrice = document.getElementsByName("adOnn").forEach(radio => {
    if (radio.checked) {
      console.log(radio.value);
      console.log(document.getElementById("totalPrice").innerHTML);
      const planPrice = document.getElementById("totalPrice").innerHTML;
      console.log(planPrice);
      document.getElementById("totalPrice").innerHTML =
        parseInt(planPrice) + parseInt(radio.value);
    }
  });
}

function backStepThree() {
  stepSummary.style.display = "none";
  stepAddOn.style.display = "flex";
  circle3.style.color = "black";
  circle3.style.backgroundColor = "rgba(255, 255, 255)";
  circle4.style.backgroundColor = "rgb(255, 255, 255, 0)";
  circle4.style.color = "white";

}

function goFromFourToTwo() {
  stepSummary.style.display = "none";
  stepPlan.style.display = "flex";
  circle2.style.color = "black";
  circle2.style.backgroundColor = "rgba(255, 255, 255)";
  circle4.style.backgroundColor = "rgb(255, 255, 255, 0)";
  circle4.style.color = "white";

}
function goToStepThankYou() {
  console.log(document.getElementById("modeResume").innerHTML);
  if (document.getElementById("modeResume").innerHTML == "Finishing up") {
    stepSummary.style.display = "flex";
    stepThankYou.style.display = "none";
  } else {
    stepSummary.style.display = "none";
    stepThankYou.style.display = "flex";
  }
}

//Check functions
checkBox = document
  .getElementById("switch")
  .addEventListener("click", event => {
    if (event.target.checked) {
      planYear.style.display = "flex";
      planMonth.style.display = "none";
      addonAnnee.style.display = "flex";
      addonMois.style.display = "none";
    } else {
      planYear.style.display = "none";
      planMonth.style.display = "flex";
      addonAnnee.style.display = "none";
      addonMois.style.display = "flex";
    }
  });

checkBox = document
  .getElementById("moisArcade")
  .addEventListener("click", event => {
    moisArcade.style.backgroundColor = "hsl(217, 100%, 97%)";
    moisArcade.style.border = " solid 1px hsl(213, 96%, 18%)";

    moisAdvenced.style.backgroundColor = "white";
    moisAdvenced.style.border = " solid 1px hsl(229, 24%, 87%)";
    moisPro.style.backgroundColor = "white";
    moisPro.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneeArcade.style.backgroundColor = "white";
    anneeArcade.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneeAdvenced.style.backgroundColor = "white";
    anneeAdvenced.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneePro.style.backgroundColor = "white";
    anneePro.style.border = " solid 1px hsl(229, 24%, 87%)";
    
  });
checkBox = document
  .getElementById("moisAdvenced")
  .addEventListener("click", event => {
    moisAdvenced.style.backgroundColor = "hsl(217, 100%, 97%)";
    moisAdvenced.style.border = " solid 1px hsl(213, 96%, 18%)";

    moisArcade.style.backgroundColor = "white";
    moisArcade.style.border = " solid 1px hsl(229, 24%, 87%)";
    moisPro.style.backgroundColor = "white";
    moisPro.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneeArcade.style.backgroundColor = "white";
    anneeArcade.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneeAdvenced.style.backgroundColor = "white";
    anneeAdvenced.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneePro.style.backgroundColor = "white";
    anneePro.style.border = " solid 1px hsl(229, 24%, 87%)";
    
  });
checkBox = document
  .getElementById("moisPro")
  .addEventListener("click", event => {
    moisPro.style.backgroundColor = "hsl(217, 100%, 97%)";
    moisPro.style.border = " solid 1px hsl(213, 96%, 18%)";
    
    moisAdvenced.style.backgroundColor = "white";
    moisAdvenced.style.border = " solid 1px hsl(229, 24%, 87%)";
    moisArcade.style.backgroundColor = "white";
    moisArcade.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneeArcade.style.backgroundColor = "white";
    anneeArcade.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneeAdvenced.style.backgroundColor = "white";
    anneeAdvenced.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneePro.style.backgroundColor = "white";
    anneePro.style.border = " solid 1px hsl(229, 24%, 87%)";
    
    
  });
checkBox = document
  .getElementById("anneeArcade")
  .addEventListener("click", event => {
    anneeArcade.style.backgroundColor = "hsl(217, 100%, 97%)";
    anneeArcade.style.border = " solid 1px hsl(213, 96%, 18%)";
   
    moisArcade.style.backgroundColor = "white";
    moisArcade.style.border = " solid 1px hsl(229, 24%, 87%)";
    moisPro.style.backgroundColor = "white";
    moisPro.style.border = " solid 1px hsl(229, 24%, 87%)";
    moisAdvenced.style.backgroundColor = "white";
    moisAdvenced.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneeAdvenced.style.backgroundColor = "white";
    anneeAdvenced.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneePro.style.backgroundColor = "white";
    anneePro.style.border = " solid 1px hsl(229, 24%, 87%)";
    
  });
checkBox = document
  .getElementById("anneeAdvenced")
  .addEventListener("click", event => {
    anneeAdvenced.style.backgroundColor = "hsl(217, 100%, 97%)";
    anneeAdvenced.style.border = " solid 1px hsl(213, 96%, 18%)";
   
    moisAdvenced.style.backgroundColor = "white";
    moisAdvenced.style.border = " solid 1px hsl(229, 24%, 87%)";
    moisPro.style.backgroundColor = "white";
    moisPro.style.border = " solid 1px hsl(229, 24%, 87%)";
    moisArcade.style.backgroundColor = "white";
    moisArcade.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneeArcade.style.backgroundColor = "white";
    anneeArcade.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneePro.style.backgroundColor = "white";
    anneePro.style.border = " solid 1px hsl(229, 24%, 87%)";
    
  });
checkBox = document
  .getElementById("anneePro")
  .addEventListener("click", event => {
    anneePro.style.backgroundColor = "hsl(217, 100%, 97%)";
    anneePro.style.border = " solid 1px hsl(213, 96%, 18%)";
  
    moisArcade.style.backgroundColor = "white";
    moisArcade.style.border = " solid 1px hsl(229, 24%, 87%)";
    moisPro.style.backgroundColor = "white";
    moisPro.style.border = " solid 1px hsl(229, 24%, 87%)";
    moisAdvenced.style.backgroundColor = "white";
    moisAdvenced.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneeArcade.style.backgroundColor = "white";
    anneeArcade.style.border = " solid 1px hsl(229, 24%, 87%)";
    anneeAdvenced.style.backgroundColor = "white";
    anneeAdvenced.style.border = " solid 1px hsl(229, 24%, 87%)";
   
  });

checkBox = document
  .getElementById("onlineMois")
  .addEventListener("click", event => {
    if (event.target.checked) {   
    } 
  });
checkBox = document
  .getElementById("storageMois")
  .addEventListener("click", event => {
    if (event.target.checked) {
      document.getElementById("storagePrice").innerHTML = "";
      document.getElementById("modeTotal").innerHTML = "";
    } else {
      document.getElementById("storagePrice").innerHTML = "";
    }
  });
checkBox = document
  .getElementById("customizableMois")
  .addEventListener("click", event => {
    if (event.target.checked) {
      document.getElementById("customizablePrice").innerHTML = "";
      document.getElementById("modeTotal").innerHTML = "";
    } else {
      document.getElementById("customizablePrice").innerHTML = "";
    }
  });
checkBox = document
  .getElementById("onlineAnnee")
  .addEventListener("click", event => {
    if (event.target.checked) {
      document.getElementById("onlinePrice").innerHTML = "";
      document.getElementById("modeTotal").innerHTML = "";
    } else {
      document.getElementById("onlinePrice").innerHTML = "";
    }
  });

document.addEventListener("DOMContentLoaded",function(){
    var selectElement=document.getElementById("levelSelect");
    selectElement.size=selectElement.size +1;
});


  // Reset functions
function reset() {
  document.getElementById("onlineMois").checked = false;
  document.getElementById("storageMois").checked = false;
  document.getElementById("customizableMois").checked = false;
  document.getElementById("onlineAnnee").checked = false;
  document.getElementById("storageAnnee").checked = false;
  document.getElementById("customizableAnnee").checked = false;
  moisArcade.style.backgroundColor = "white";
  moisArcade.style.border = " solid 1px hsl(229, 24%, 87%)";
  moisPro.style.backgroundColor = "white";
  moisPro.style.border = " solid 1px hsl(229, 24%, 87%)";
  moisAdvenced.style.backgroundColor = "white";
  moisAdvenced.style.border = " solid 1px hsl(229, 24%, 87%)";
  anneeArcade.style.backgroundColor = "white";
  anneeArcade.style.border = " solid 1px hsl(229, 24%, 87%)";
  anneeAdvenced.style.backgroundColor = "white";
  anneeAdvenced.style.border = " solid 1px hsl(229, 24%, 87%)";
  anneePro.style.backgroundColor = "white";
  anneePro.style.border = " solid 1px hsl(229, 24%, 87%)";
}

//Error functions
function checkName() {
  let myNameInput = document.getElementById("infoName");
  let myNameError = document.getElementById("errorName");
  let myNameRegex = /^[a-zA-Z-\s]+$/;

  if (myNameInput.value.trim() == "") {
    myNameError.innerHTML = "This field is required";
  } else if (myNameRegex.test(myNameInput.value) == false) {
    myNameError.innerHTML = "Can't contain numbers or symbols";
  } else if (myNameInput.value.trim() !== "") {
    myNameError.innerHTML = "";
  }
}

function checkNum() {
  let myNumInput = document.getElementById("infoNumber");
  let myNumError = document.getElementById("errorNum");
  let myNumRegex = /^[0-9\s]+$/;

  if (myNumInput.value.trim() == "") {
    myNumError.innerHTML = "This field is required";
  } else if (myNumRegex.test(myNumInput.value) == false) {
    myNumError.innerHTML = "Must contain number";
  } else if (myNumInput.value.trim().length !== 12) {
    myNumError.innerHTML = "Invalid index number length";
  } else {
    myNumError.innerHTML = "";
  }
}

function Achieve() {
  let myNumInput = document.getElementById("infoNumber");
  let myNameInput = document.getElementById("infoName");
  
  let myNameRegex = /^[a-zA-Z-\s]+$/;
  let myNumRegex = /^[0-9\s]+$/;
 
  if (
    myNumInput.value.trim().length === 12 &&
    myNumRegex.test(myNumInput.value) == true &&
  
    myNameInput.value.trim().length !== 0 &&
    myNameRegex.test(myNameInput.value) === true
  ) {
    stepInfo.style.display = "none";
    stepPlan.style.display = "flex";
    circle1.style.color = "white";
    circle1.style.backgroundColor = "rgba(255, 255, 255, 0)";
    circle2.style.backgroundColor = "rgb(255, 255, 255)";
    circle2.style.color = "black";
  }
}

function checkPlan() {
  if (document.getElementById("modeResume").innerHTML == "Kindly choose your conplaint type") {
    stepInfo.style.display = "none";
    stepPlan.style.display = "flex";
    circle1.style.color = "white";
    circle1.style.backgroundColor = "rgba(255, 255, 255, 0)";
    circle2.style.backgroundColor = "rgb(255, 255, 255)";
    circle2.style.color = "black";
  } else {
    stepPlan.style.display = "none";
    stepAddOn.style.display = "flex";
    circle2.style.color = "white";
    circle2.style.backgroundColor = "rgba(255, 255, 255, 0)";
    circle3.style.backgroundColor = "rgb(255, 255, 255)";
    circle3.style.color = "black";
  }
}


