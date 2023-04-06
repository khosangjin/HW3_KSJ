def reverse_words(str):
    strList = str.split();
    strList.reverse();
    res = "";
    for i in strList:
        res = res + i + " ";
    return res

if __name__ == "__main__" :
    str1 = ("Two roads diverged in a yellow wood, And sorry I could not travel both And "
    + "be one traveler, long I stood And looked down one as far as I could To where "
    + "it bent in the undergrowth");
    str2 = ("Then took the other, as just as fair, And having perhaps the better claim, "
    + "Because it was grassy and wanted wear; Though as for that the passing there "
    +"Had worn them really about the same");

    res1 = reverse_words(str1);
    res2 = reverse_words(str2);

    print("<original>");
    print(str1);
    print("\n");
    print("<reverse version>");
    print(res1);
    print("\n");
    print("==================================")
    print("<original>");
    print(str2);
    print("\n");
    print("<reverse version>");
    print(res2);
    print("\n");
