// Copyright (c) 2023 Mohamad All rights reserved
//
// Created by: Mohamad
// Created on: Sep 2023
// This file contains the JS functions for index.html

// Basic math
function mathButtonClicked() {
  document.getElementById("add-math").innerHTML = "<p>1 + 3 = " + (1 + 3) + "</p>"
  document.getElementById("subtract-math").innerHTML = "<p>2 - 4 =  " + (2 - 4) + "</p>"  
  document.getElementById("multiply-math").innerHTML = "<p>3 * 5 = " + (3 * 4) + "</p>" 
  document.getElementById("divide-math").innerHTML = "<p>6 / 2 = " + (6 / 2) + "</p>"
  document.getElementById("exponent-math").innerHTML = "<p>2^3 + 1 = " + (2 ** 3 + 1) + "</p>"
// Create notification after button is clicked
  document.getElementById("solved").innerHTML = "Solved!"
}
