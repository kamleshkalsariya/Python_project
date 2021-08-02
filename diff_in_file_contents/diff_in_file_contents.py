"""
Find differences in file contents.
"""


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    len1 = len(line1)
    len2 = len(line2)
    length = min(len1, len2)
    if(length == 0 and line1 != line2):
        identical = 0
    else:
        identical = -1

    for index in range(length):
        if(len1 == len2):
            if(line1[index] == line2[index]):
                identical = -1

            else:
                identical = index
                break
        else:
            if(line1[index] == line2[index]):
                identical = index + 1

            else:
                identical = index
                break
    return identical
#line1 = "asdf"
#line2 = "asfg"
#Output = singleline_diff(line1,line2)
#print(Output)

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    output = singleline_diff(line1, line2)
    str1 = ""
    len1 = len(line1)
    len2 = len(line2)
    length2 = min(len1, len2)
    if(length2 == 0 and line1 != line2):
        str1 = line1+"\n"+"="*output+"^"+"\n"+line2+"\n"
    elif(length2 == 0 and line1 == line2):
        str1 = line1+"\n"+"="*output+"^"+"\n"+line2+"\n"
    for index in range(length2):
        if(line1[index] == "\n or \r" or line2[index] == "\n or \r"):
            pass

        else:
            if(idx != -1 and idx <= length2):
                str1 = line1+"\n"+"="*idx+"^"+"\n"+line2+"\n"



    return str1
#singleline_diff_format('abc', 'abd', 2)
#singleline_diff_format(line1,line2,Output)

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    identical = -1
    identical1 = -1
    len1 = len(lines1)
    len2 = len(lines2)
    length3 = min(len1, len2)
    if(length3 == 0 and lines1 != lines2):
        identical = 0
        identical1 = 0
    elif(length3 == 0 and lines1 == lines2):
        identical = -1
        identical1 = -1
    for index in range(length3):
        output = singleline_diff(lines1[index], lines2[index])
        if(len1 == len2):
            if (output == -1):
                pass
            else:
                identical = index
                identical1 = output
                break
        else:
            #output = singleline_diff(lines1[index], lines2[index])
            if(output != -1):
                identical = index
                identical1 = output
            else:
                identical = length3
                identical1 = 0


    return (identical, identical1)



def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lst = []
    lst3 = []

    openfile = open(filename, "rt")
    data = openfile.read()
    if(len(data) != 0):
        if(data[-1] != "\n"):
            length5 = len(data)
        else:
            length5 = len(data) - 1
    else:
        length5 = -1
    for index in range(length5):
        if(len(data) != 0):
            lst += data[index]
    if(len(data) != 0):
        lst2 = ("".join(lst))
        lst3 = (lst2.split("\n"))
    openfile.close()
    return lst3


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    str2 = "No differences\n"
    lst1 = get_file_lines(filename1)
    lst2 = get_file_lines(filename2)
    lenght3 = min(len(lst1), len(lst2))
    for index in range(lenght3):
        output1 = singleline_diff(lst1[index], lst2[index])
        if (output1 != -1):
            str2 = "Line "+str(index)+":"+"\n"+singleline_diff_format(lst1[index], lst2[index], output1)
            break
    return str2

