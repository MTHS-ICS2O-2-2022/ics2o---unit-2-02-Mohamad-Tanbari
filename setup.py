import os
import sys

# Print welcome message
print("0;33mWelcome to the website setup program! - Mohamad0;33m")

# Ask user if they want to create a new website
create = input("\033[92mDo you want to create a new website? (y/n) \033[0m")
if input(create) == "n":  # If the user doesn't want to create a new website
    sys.exit()  # Exit the program
if input(create) == "y":  # If the user wants to create a new website
    print("\033[92mLoading... \033[0m")

# Code to paste into index.html, style.css, and script.js
htmlContent = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-9" />
    <meta name="description" content="{$websiteDescription}" />
    <meta name="keywords" content="mths, ics2o" />
    <meta name="author" content="Mohamad" />
    <meta name="viewport" conent="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/icon?family=Material+Icons"
    />
    <link
      rel="stylesheet"
      href="https://code.getmdl.io/1.3.0/material.lime-green.min.css"
    />
    <link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png" />
    <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png" />
    <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png" />
    <link rel="manifest" href="site.webmanifest" />
    <link rel="stylesheet" href="css/style.css" />
    <title>{$websiteTitle}</title>
  </head>
  <body>
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    <script src="./js/script.js"></script>
    <!-- Always shows a header, even in smaller screens. -->
    <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
      <header class="mdl-layout__header">
        <div class="mdl-layout__header-row">
          <!-- Title -->
          <span class="mdl-layout-title">{$websiteHeader}</span>
          <!-- Add spacer, to align navigation to the right -->
          <div class="mdl-layout-spacer"></div>
          <!-- Navigation. We hide it in small screens. -->
          <nav class="mdl-navigation mdl-layout--large-screen-only">
            <a class="mdl-navigation__link" href=""></a>
            <a class="mdl-navigation__link" href=""></a>
            <a class="mdl-navigation__link" href=""></a>
            <a class="mdl-navigation__link" href=""></a>
          </nav>
        </div>
      </header>
      <div class="mdl-layout__drawer">
        <span class="mdl-layout-title">Navigate</span>
        <nav class="mdl-navigation">
          <a class="mdl-navigation__link" href="./index2.html"
            >Second Website</a
          >
        </nav>
      </div>
      <main class="mdl-layout__content">
        <div class="page-content">
          <!--Donut picture-->
          <img src="./images/donut.png" alt="Donut" class="donut" />
          <!--Text below header-->
          <div class="page-content">Enter number to calculate</div>
          <!-- Numeric Textfield with Floating Label -->
          <form action="#">
            <div
              class="mdl-textfield mdl-js-textfield mdl-textfield--floating-label"
            >
              <input
                class="mdl-textfield__input"
                type="text"
                pattern="-?[0-9]*(\.[0-9]+)?"
                id="sample4"
              />
              <label class="mdl-textfield__label" for="sample4"
                >Number...</label
              >
              <span class="mdl-textfield__error">Input is not a number!</span>
            </div>
          </form>
          <!-- Accent-colored raised button with ripple -->
          <button
            class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent"
            onclick="buttonClicked()"
          >
            Calculate
          </button>
        </div>
        <!--Answer output from button-->
        <div class="page-content">The answer is ...</div>
      </main>
    </div>
  </body>
</html>
"""

cssContent = """/* Created by: Mohamad
* Created on: Sep 2023
* This file contains the CSS for index.html
*/

.page-content {
  padding: 15px;
}

.donut {
  float: right;
}
"""

jsContent = """// Copyright (c) 2023 Mohamad All rights reserved
//
// Created by: Mohamad
// Created on: Sep 2023
// This file contains the JS functions for index.html
function buttonClicked() {
}
"""

# Path to index.html
indexHtmlPath = os.path.join(os.getcwd(), "index.html")

# Path to style.css
styleCssPath = os.path.join(os.getcwd(), "css", "style.css")

# Path to script.js
scriptJsPath = os.path.join(os.getcwd(), "js", "script.js")

# Delete contents of index.html
with open(indexHtmlPath, "w") as f:
    f.write("")

# Delete contents of style.css
with open(styleCssPath, "w") as f:
    f.write("")

# Delete contents of script.js
with open(scriptJsPath, "w") as f:
    f.write("")

# Add HTML to index.html
with open(indexHtmlPath, "a") as f:
    f.write(htmlContent)

# Add CSS to style.css
with open(styleCssPath, "a") as f:
    f.write(cssContent)

# Add JavaScript to script.js
with open(scriptJsPath, "a") as f:
    f.write(jsContent)

# Print "Done" in green
print("\033[92mDone\033[0m")

# Ask for website title
title = input("\033[92mWhat do you want the title of the website to be? \033[92m")

# Replace "{$websiteTitle}" with user"s input in index.html
with open(indexHtmlPath, "r") as f:
    html = f.read()
html = html.replace("{$websiteTitle}", title)
with open(indexHtmlPath, "w") as f:
    f.write(html)

# Ask for website description
title = input("\033[92mWhat do you want the description of the website to be? \033[92m")

# Replace "{$websiteDescription}" with user"s input in index.html
with open(indexHtmlPath, "r") as f:
    html = f.read()
html = html.replace("{$websiteDescription}", title)
with open(indexHtmlPath, "w") as f:
    f.write(html)

# Ask for website heading
title = input("\033[92mWhat do you want the header of the website to be? \033[92m")

# Replace "{$websiteHeader}" with user"s input in index.html
with open(indexHtmlPath, "r") as f:
    html = f.read()
html = html.replace("{$websiteHeader}", title)
with open(indexHtmlPath, "w") as f:
    f.write(html)

# Print "Done" in green
print("\033[92mDone\033[0m")
