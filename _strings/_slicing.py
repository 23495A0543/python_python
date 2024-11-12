

sentence = "This is srinivas Developer"
print(sentence[0] + sentence[1]) 

#syntax --> var[start:stop:step]
#syntax --> var[start:stop]
    
    
    
    #-------------------POSITIVE SLICING-----------------
print(sentence[0:len(sentence):1])  # if we can't enter step value defalut it is 1
print(sentence[7:])  #  if we can not enter stop value is defalut to took length of sentence
print(sentence[:])   # if we can't  enter any values its took whole sentence when we use colon





    #---------------------NEGATIVE SLICING------------------------
sentence = "This is srinivas Developer"
print(f"=====negative slicing========")
print(sentence[:])
print(sentence[-10:-1])
print(sentence[-4::2])
print(sentence[-1::-1])
print(sentence[-11:-5])
print(sentence[::])
print(sentence[:])