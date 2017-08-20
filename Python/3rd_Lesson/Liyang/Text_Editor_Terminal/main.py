#!/usr/bin/python 
# -*- codig:UTF-8 -*-

import time
import pyperclip

def ask_path():
  print '================================================================='
  print '|                                                               |'
  print '|                          welcome                              |'
  print '|                            to                                 |'
  print '|                           Lime                                |'
  print '|                                                               |'
  print '|                  An excellent text editor                     |'
  print '|                                                               |'
  print '=================================================================' 
  #welcome panel
  print 'please input the file path and name you need to open'
  print '(Eg. "user/mydata/file_name")'
  path_name = raw_input('>')
  return path_name

def update_data(old_data):
  pyperclip.copy(old_data)
  print '(Press "Ctrl + V" to enable the editor, press "ENTER" to end the edit)'
  print '=========================edit begin=============================='
  new_data = raw_input('>>') 
  print '************************ edit end *******************************'
  change_data = get_change_data(old_data, new_data) 
  return new_data, change_data

def get_change_data(old_data, new_data):
  if old_data != new_data:
    change_data = '-------------\n'+ old_data + '\n-------------\n|  |  |\n|  |  |\nV  V  V \
                  \n-------------\n' + new_data + '\n-------------\n'
  return change_data

def get_history_file_path(input_path):
  record_number = -1 
  for search_number in range(len(input_path)):
    if input_path[search_number] == '/':
      record_number = search_number
  if record_number == -1:
    return_path = '.history_' + input_path
  else:
    return_path = input_path[:record_number+1] +'.history_' \
                + input_path[record_number+1:]
  return return_path

def transform_record_str(change_str):
  record_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) \
             + '\n#####\n' + change_str + '*****\n\n\n'
  return record_str



if __name__ == "__main__":
  #ask the user what the filename and path should be
  data_file_path = ask_path()

  #check if it is a new file to creat
  check_file = open(data_file_path,'a+')
  check_file.close()

  while True:
    #open the data file for read
    text_file_read = open(data_file_path)

    #save its content in a temperary space
    temperary_data = text_file_read.read()
    #print it's content on screen 
    print '-------------------------text content------------------------------'
    print temperary_data
    print '-------------------------end of the text---------------------------'
    #close the file open for read
    text_file_read.close()

    #ask if the user mean to change the content
    print 'Do you want to change the file?(Y/N)'
    jud_change = raw_input('>')

    #if so
    if 'Y' == jud_change or 'y' == jud_change or '' == jud_change:
      #creat or add contnet to the history record file 
      history_file_path = get_history_file_path(data_file_path)
      history_file = open(history_file_path, 'a+')
      #open the data file to write
      text_file_write = open(data_file_path, 'w')
      #enter the editor panel
      new_data, change_data = update_data(temperary_data)
      #change the content 
      text_file_write.write(new_data)
      #record the change
      record_change_str = transform_record_str(change_data)
      history_file.write(record_change_str)
  
      #colse all the file 
      history_file.close()
      text_file_write.close()
    else:
      print '+++++++++++++++++++++++++++++++++++++++++++++'
      print 'okay, terminal shot down...'
      print '+++++++++++++++++++++++++++++++++++++++++++++\n'
      break