sentence="Sky is Blue water is color less"
word_count={word:len(word) for word in sentence.split()}
print(word_count)


temp_c={"mon":30,"tue":28,"wed":24,"thu":34,"fri":31,"sat":30,"sun":29}
temp_f={day:temp*9/5+32 for (day,temp) in temp_c.items()}
print(temp_f)