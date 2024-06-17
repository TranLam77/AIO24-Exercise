def calculate_f1_score(tp,fp,fn):
    #Check if type of parameters tp, fp, fn is int
    if type(tp) != int:
      print('tp must be int')
      return
    if type(fp) != int:
      print('fp must be int')
      return
    if type(fn) != int:
      print('fn must be int')
      return

    #Check if parameters tp, fp, fn <= 0
    if tp <= 0 or fp <= 0 or fn <= 0:
      print('tp and fp and fn must be greater than zero')
      return

    #Calculate precision, recall, f1_score
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*precision*recall/(precision+recall)
    print(f"Precision is {precision}")
    print(f"Recall is {recall}")
    print(f"F1-score is {f1_score}")

calculate_f1_score(2,4,5)