// Copyright (c) 2023 Mohamad All rights reserved
//
// Created by: Mohamad
// Created on: Sep 2023
// This file contains the JS functions for index.html

function mathButtonClicked() {
  document.getElementById("area").innerHTML = "Area of rectangle: = " + (5 * 3) + " cm²</p>"
  document.getElementById("perimeter").innerHTML = "Perimeter of rectangle: = " + (2 * (5 + 3)) + " cm</p>"
  // Create notification after button is clicked
  document.getElementById("solved").innerHTML = "Solved!"
}
