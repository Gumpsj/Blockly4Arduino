# Blockly4Arduino
Code repo of [Ingegno](http://ingegno.be) website with [Blockly](https://developers.google.com/blockly/) for [Arduino](http://arduino.cc) 

This is the code of website [Ingegno Blockly4Arduino](http://ingegno.be/Manuals/Blockly4Arduino/demos/blocklyduino/), created for the LedUpKidz project.

*Blockly for Arduino or Genuino* allows to program your Arduino with blocks, ideal for novices to learn the basics. Blockly for Arduino is also touch friendly so can be used on a tablet.

At the moment it is aimed at the LedUpKidz project of Ingegno, so as to allow to program your LedUpKidz graphically. 

## Translations
Would you like to submit a translation of the website for your language? This can be done easily:
1. from [our blockly branch](https://github.com/bmcage/blockly/tree/arduino/msg/json) copy from the file en.json the string codes starting with `ARD`, as well as the codes under those, to your language file, eg `de.json`
2. Translate them. 
3. Send them to us, or do a pull request against our branch of blockly.

We plan to make the demo site more easily translatable. At the moment, to obtain a version for your language, you need to create a copy of this repo, and create a copy of Blockly4Arduino [index_en.html](https://github.com/ingegno/Blockly4Arduino/blob/master/Blockly4Arduino/demos/blocklyduino/index_en.html) and translate the few strings present. See the Dutch site for such a translation: [index.html](https://github.com/ingegno/Blockly4Arduino/blob/master/Blockly4Arduino/demos/blocklyduino/index.html).


## Screenshots

![](https://github.com/ingegno/Blockly4Arduino/blob/master/doc/blockly_ex1.png?raw=true)

![](https://github.com/ingegno/Blockly4Arduino/blob/master/doc/blockly_ex2.png?raw=true)

![](https://github.com/ingegno/Blockly4Arduino/blob/master/doc/blockly_ex3.png?raw=true)

# For developers

The code is based on the branch *arduino* from [bmcage/blockly](https://github.com/bmcage/blockly). The directory structure locally should be:

`./git/blockly` (branch arduino from [bmcage](https://github.com/bmcage/blockly))

`./git/closure-library` (from [google](https://github.com/google/closure-library))

`./git/Blockly4Arduino`

In blockly run `python build.py` to build blockly. In Blockly4Arduino run `python create_site.py`, which will update Blockly4Arduino with the files needed for the website.

