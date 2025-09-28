#!/usr/bin/env python3

import re
class MyString:
  def __init__(self,value = ""):
    self.value = value
   
  @property
  def value (self):
    return self._value
  
  @value.setter
  def value(self,value):
    if isinstance(value,str):
      self._value = value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")

  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    new_sentences = re.split(r'[?.!]',self.value)
    new_sentences= [s.strip() for s in new_sentences if s.strip()]
    return len(new_sentences)
  
mystring= MyString("He!My name is Ethan.What is yours?You look hungry.Want some food?")

mystring.is_sentence()
mystring.is_question()
mystring.is_exclamation()
mystring.count_sentences()
  
  