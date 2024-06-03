##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##
                                                 ##MATRIX CALCULATOR
##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##

from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("MATRIX CALCULATOR")

##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##
                                            ##Defining Recurring Functions
##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##

def destroy():
    for i in e_frame.winfo_children():  ## children widgets of e_frame
        if isinstance(i, Label) or isinstance(i, Entry) or isinstance(i, LabelFrame) or isinstance(i, Button): ##separately because don't want to destroy the frame
            i.destroy()
            # root.update_idletasks()

def user_mat_choice(mat_function): ##called by transpose, det, inverse, edit, cofactors
    global matrices
    global e_screen
    global function
    destroy()
    matrices = {1: "MatA", 2: "MatB", 3: "MatC", 4: "MatD"}
    Label(e_frame, text="Choose the matrix for " + str(mat_function),bg="#203873", fg="white",
          font=("Aerial", 10, "bold"), anchor=CENTER, width=30, height=2).grid(row=0,column=0,padx=40,pady=3,columnspan=2)

    ##to display names of matrices to be chosen by the user
    for i in range(1, len(matrices) - 1):
        a = str(i) + "  :  " + str(matrices.get(i))
        Label(e_frame, text=a, font=("Aerial", 10, "bold"), anchor=W, width=17,
              bg="#203873", fg="white", height=2).grid(row=i, column=0, padx=9, pady=13)
    for j in range(3, len(matrices) + 1):
        a = str(j) + "  :  " + matrices.get(j)
        Label(e_frame, text=a, font=("Aerial", 10, "bold"), anchor=W, width=17,bg="#203873", fg="white", height=2).grid(row=j - 2, column=1,
                                                                                               padx=9, pady=13)

    e_screen = Entry(e_frame, width=20, font=("Aerial", 7), bg="#A3A3A3", borderwidth=3)
    e_screen.grid(row=4, column=0, pady=20, padx=5, columnspan=2)
    if mat_function=="Determinant":
        function="user_mat_choice_d"
    elif mat_function=="Transposition":
        function="user_mat_choice_t"
    elif mat_function=="Inverse":
        function="user_mat_choice_i"
    elif mat_function=="Edit":
        function="user_mat_choice_e"
    elif mat_function=="Cofactors":
        function="user_mat_choice_c"

def user_matrix_choice1():  ##called by transpose, det, inverse, edit, cofactors
    import copy
    user_option = int(e_screen.get())
    if user_option == 1:
        mat_u = copy.deepcopy(MatA) ##without this same the matrix inverse values are also inserted in this matrix; MatA
        name_u = "MatA"
    elif user_option == 2:
        mat_u = copy.deepcopy(MatB)
        name_u = "MatB"
    elif user_option == 3:
        mat_u = copy.deepcopy(MatC)
        name_u = "MatC"
    elif user_option == 4:
        mat_u = copy.deepcopy(MatD)
        name_u = "MatD"
    else:
        mat_u = []
        name_u = ""
    return mat_u, name_u

def display(function_name, name_mat, mat ): ##used by - transpose display, mat_mult, mat_add, inverse, mat_ans, edit
    destroy()
    matrix_display = LabelFrame(e_frame, height=230, width=320,
                                bg="#203873")  ##a new frame created to contain matrix so that entry box remains at the bottom
    matrix_display.grid(row=0, column=0, padx=10, pady=10)
    matrix_display.grid_propagate(FALSE)

    Label(matrix_display, text="The {0} {1} is: ".format(function_name, name_mat),
          font=("Aerial", 10, "bold"), bg="#203873",fg="white", anchor=CENTER, width=30, height=2).grid(row=0, column=0, padx=40, pady=3,
                                                                               columnspan=len(mat[0]))
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            ## displaying matrix rows and columns
            Label(matrix_display, text=str(round(mat[i][j],5)), bg="#3873a1", height=2, width=10,
                  font=("Aerial", 7)).grid(row=i + 1, column=j, padx=3, pady=5)

def forward(op,wt): ##recieving second argument so that value is to be transformed x is not added instead of + due to same condition of function==forward in click
    global function
    global e_function

    if wt == "add":
        function = "forward_add"
    elif wt== "mult":
        function = "forward_mult"
    e_function="forward"
    for i in e_frame.winfo_children():  ## children widgets of e_frame
        if isinstance(i, Label) or isinstance(i, Button):
            i.destroy()
            root.update_idletasks()  ## check this

    matrices_inverse = {1: "MatAi", 2: "MatBi", 3: "MatCi", 4: "MatDi"}
    Label(e_frame, text="Choose the matrices for {}".format(op), font=("Aerial", 10, "bold"), bg="#203873",
          fg="white", anchor=CENTER,
          width=30, height=2).grid(row=0, column=0, padx=40, pady=3, columnspan=2)

    for x in range(1, len(matrices_inverse) - 1):
        b = str(x) + "  :  " + str(matrices_inverse.get(x))
        Label(e_frame, text=b, font=("Aerial", 10, "bold"), anchor=W, width=17, height=2, bg="#203873",
              fg="white").grid(row=x, column=0, padx=9,
                               pady=13)
    for y in range(3, len(matrices_inverse) + 1):
        b = str(y) + "  :  " + matrices_inverse.get(y)
        Label(e_frame, text=b, font=("Aerial", 10, "bold"), anchor=W, width=17, height=2, bg="#203873",
              fg="white").grid(row=y - 2, column=1,
                               padx=9, pady=13)

    Button(e_frame, text="<<", width=10, height=1, bg="#3873a1", borderwidth=3, activebackground="#2C5656",
           command=lambda: user_mat_choice_mult_add(op, "forward")).grid(row=5,sticky=SW, column=0)

def user_mat_choice_mult_add(operation, where):
    global matrices
    global e_screen
    global e_function
    global function

    if where=="forward":  ##so that entry box is saved only when getting back from forward function
        for i in e_frame.winfo_children():  ## children widgets of e_frame
            if isinstance(i, Label) or isinstance(i, Button):    ##so that entry box is not deleted
                i.destroy()
                root.update_idletasks()
    else:
        destroy()
        e_screen = Entry(e_frame, width=35, font=("Aerial", 12), bg="#A3A3A3", borderwidth=3)
        e_screen.grid(row=4, column=0, pady=20, padx=5, columnspan=2)

    matrices = {1: "MatA", 2: "MatB", 3: "MatC", 4: "MatD"}
    Label(e_frame, text="Choose the matrices for {}".format(operation), font=("Aerial", 10, "bold"),bg="#203873", fg="white",
          anchor=CENTER,
          width=30, height=2).grid(row=0, column=0, padx=40, pady=3, columnspan=2)

    ##to display names of matrices to be chosen by the user
    for i in range(1, len(matrices) - 1):
        a = str(i) + "  :  " + str(matrices.get(i))
        Label(e_frame, text=a, font=("Aerial", 10, "bold"), anchor=W, width=17, height=2,bg="#203873",
              fg="white").grid(row=i, column=0, padx=9,pady=13)
    for j in range(3, len(matrices) + 1):
        a = str(j) + "  :  " + matrices.get(j)
        Label(e_frame, text=a, font=("Aerial", 10, "bold"), anchor=W, width=17, height=2,bg="#203873",
              fg="white").grid(row=j - 2, column=1, padx=9, pady=13)

    e_function="backward"
    if operation == "Multiplication":
        function = "user_mat_choice_mult"
    elif operation == "Addition":
        function = "user_mat_choice_add"

    Button(e_frame, text=">>", width=3, height=1, bg= "#3873a1",padx=30, borderwidth=3, activebackground="#2C5656",
           command=lambda: forward(operation, where)).grid(row=5, column=1, sticky=SE)

##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##
                                            ##Defining Matrix Functions
##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##


##1 (a)
def define_matrix1():
    global e_screen
    global function
    global matrices
    global b_enter
    b_enter.config(state="disabled")
    matrices = {1: "MatA", 2: "MatB",3: "MatC", 4: "MatD"}
    destroy()
    #heading
    Label(e_frame, text="Define Matrix:", font=("Aerial", 10, "bold"), bg="#203873", fg="white", anchor=CENTER, width=20,
          height=2).grid(row=0, column=0, padx=40, pady=3, columnspan=2)
    ##to display names of matrices to be chosen by the user
    for i in range(1, len(matrices)-1):
        a=str(i)+ "  :  " + str(matrices.get(i))
        Label(e_frame, text=a, font=("Aerial", 10, "bold"),bg="#203873", fg="white", anchor=W, width=17, height=2).grid(row=i, column=0, padx=9, pady=13)
    for j in range(3, len(matrices)+1):
        a=str(j)+ "  :  " + matrices.get(j)
        Label(e_frame, text=a, font=("Aerial", 10, "bold"),bg="#203873", fg="white",anchor=W, width=17, height=2).grid(row=j-2, column=1, padx=9, pady=13)

    e_screen=Entry(e_frame, width=20, font=("Aerial", 7),bg="#A3A3A3", borderwidth=3)
    e_screen.grid(row=4, column=0, pady=20, padx=5, columnspan=2)
    function = "define_matrix1"  ##next button to be clicked

##1(b)
def define_rc(string_row, string_col):
    global e_screen
    global e_function
    global name
    global b_enter
    global b_next

    b_next.config(state="disabled")

    if string_row == "Number of rows":
        e_function = "define_rc"  ##when enter is clicked
        operation="Define"
    elif string_row == "Select the Row Number":
        e_function = "define_rc_edit"
        operation="Edit"
    else:
        operation=""
    b_enter.config(state="normal")
    try:
        matrix_no = int(e_screen.get())
        name = matrices.pop(matrix_no)
    except KeyError:
        pass
    except ValueError:
        pass
    finally:
        destroy()
        Label(e_frame, text="{0} {1}".format(operation, name), font=("Aerial", 10, "bold"),bg="#203873", fg="white",anchor=CENTER,
              width=20, height=2).grid(row=0, column=0, padx=70, pady=5, columnspan=2)

        Label(e_frame, text="{0} : {1}".format(name, string_row), font=("Aerial", 10, "bold"), anchor=W,bg="#203873", fg="white",
              width=27,height=2).grid(row=1, column=0, padx=2, pady=15)
        Label(e_frame, text="{0} : {1}".format(name, string_col), font=("Aerial", 10, "bold"), anchor=W,bg="#203873", fg="white",
              width=27,height=2).grid(row=2, column=0, padx=2, pady=15)

        e_screen = Entry(e_frame, width=20, font=("Aerial", 7), bg="#A3A3A3", borderwidth=3)
        e_screen.grid(row=4, column=0, padx=5, pady=20, columnspan=2)

##1 (c)
def define_matrix_display():
    global el
    global e_screen
    global e_function
    global labels
    global function
    global b_enter
    global entry_num_list

    b_enter.config(state="normal")
    entry_num_list=[]

    destroy()
    try:
        row=rc[0]
        col = rc[1]
    except IndexError:
        messagebox.showerror("Error!", "Row and column of the matrix were not defined properly; Try Again")
        define_matrix1()
    else:
    ##forming widgets
        matrix_display=LabelFrame(e_frame,height=220, width=320, bg="#203873") ##a new frame created to contain matrix so that entry box remains at the bottom
        matrix_display.grid(row=0, column=0, padx=10, pady=10)
        matrix_display.grid_propagate(FALSE)
        e_screen = Entry(e_frame, width=40, font=("Aerial", 10), bg="#A3A3A3", borderwidth=3)
        e_screen.grid(row=1, column=0, padx=5, pady=5)

        Label(matrix_display,fg="white", bg="#203873", text="Define {0} of {1} x {2} order".format(name, row, col),
              font=("Aerial", 10, "bold"), anchor=CENTER, width=25, height=2).grid(row=0, column=0, padx=40, pady=3, columnspan=col)
        labels=[]
        for i in range(row):
            for j in range(col):
                ## displaying matrix rows and columns to be filled in by the user
                el=Label(matrix_display, text="0", height=2, bg="#3873a1",width=10, font=("Aerial", 7))
                el.grid(row=i+1, column=j, padx=3, pady=5)
                labels.append(el)

        e_function="define_matrix_display"
        function="define_matrix_display"

##1 (d)  ##the main program to define the matrix
def define_matrix():
    global entry_num_list
    global function
    global Mat_ans
    row = rc[0]
    col = rc[1]
    matrix = []
    for i in range(row):
        matrix_row = []
        for j in range(col):
            if len(entry_num_list)!=0:
                matrix_row.append(entry_num_list[0])
                entry_num_list.remove(entry_num_list[0])
        matrix.append(matrix_row)

    global MatA
    global MatB
    global MatC
    global MatD
    Mat_ans=matrix
    if name == "MatA":
        MatA = matrix
    elif name == "MatB":
        MatB = matrix
    elif name == "MatC":
        MatC = matrix
    elif name == "MatD":
        MatD = matrix

##2
def edit(where): ##so that only one function is used

    def replacing_element(mat):
        try:
            mat[rc[0]-1][rc[1]-1]=rc[2]
            return mat
        except IndexError:
            messagebox.showerror("Dimension Error!", "No element at this position")
        except ValueError:
            messagebox.showerror("Error!", "Wrong button clicked")

    global Mat_ans
    global name
    global MatA
    global MatB
    global MatC
    global MatD

    if where=="initial":
        Mat_ans, name=user_matrix_choice1()
        if name=="":
            messagebox.showerror("Error!", "Wrong value")
        else:
            define_rc("Select the Row Number", "Select the Column Number")

    elif where=="to_edit":
        mat_e=replacing_element(Mat_ans)
        display("Editted", name, mat_e)
        Mat_ans=mat_e
        if name=="MatA":
            MatA=mat_e
        elif name=="MatB":
            MatB=mat_e
        elif name=="MatC":
            MatC=mat_e
        elif name=="MatD":
            MatD=mat_e

##3
def matrix_addition():
    global Mat_ans
    global function
    function = "matrix_addition" ##to give delete specific functionality
    def matrix_addition1(a, b):
        mat = []
        if len(a) == len(b) and len(a[0]) == len(b[0]):
            for i in range(len(a)):
                k = []
                for j in range(len(a[0])):
                    ans = a[i][j] + b[i][j]
                    k.append(ans)
                mat.append(k)

        else:
            mat="Dimension Error"
        return mat

    global resultant_matrix_add

    mm_list = (e_screen.get()).split(" +  ")

    for index, value in enumerate(mm_list):  ## replacing strings in the list with their corresponding matrix
        if value == "MatA":
            mm_list[index] = MatA
        elif value == "MatB":
            mm_list[index] = MatB
        elif value == "MatC":
            mm_list[index] = MatC
        elif value == "MatD":
            mm_list[index] = MatD
        elif value == "MatAi":
            mm_list[index] = MatAi
        elif value == "MatBi":
            mm_list[index] = MatBi
        elif value == "MatCi":
            mm_list[index] = MatCi
        elif value == "MatDi":
            mm_list[index] = MatDi
        else:
            mm_list.remove(value)
    try:
        resultant_matrix_add = mm_list[0]
        for x in range(1, len(mm_list)):
            resultant_matrix_add = matrix_addition1(resultant_matrix_add, mm_list[x])

            if resultant_matrix_add=="Dimension Error":
                break
        if resultant_matrix_add=="Dimension Error":
            messagebox.showerror("Dimension Error", "The order of the matrices must be same for Addition")
            options()
        else:
            display("Result of", "Matrix Addition", resultant_matrix_add)
            Mat_ans=resultant_matrix_add
    except IndexError:  ##if user goes on with addition without defining matrices
        messagebox.showerror("Dimension Error", "The matrix is undefined")
        options()
#
# ##4
def matrix_multiplication():
    global Mat_ans
    def matrix_multiplication1(x, y):
        r = []

        if len(x[0]) == len(y):
            for i in range(len(x)):
                r_row = []
                for k in range(len(y[0])):
                    y_col = 0
                    for j in range(len(y)):
                        a = (x[i][j]) * (y[j][k])
                        y_col = y_col + a
                    fvalue = y_col
                    r_row.append(fvalue)
                r.append(r_row)
        else:
            r="Dimension Error"
        return r
    global resultant_matrix_mult

    mm_list = (e_screen.get()).split(" x  ")
    for index, value in enumerate(mm_list):
        if value == "MatA":
            mm_list[index] = MatA
        elif value == "MatB":
            mm_list[index] = MatB
        elif value == "MatC":
            mm_list[index] = MatC
        elif value == "MatD":
            mm_list[index] = MatD
        elif value == "MatAi":
            mm_list[index] = MatAi
        elif value == "MatBi":
            mm_list[index] = MatBi
        elif value == "MatCi":
            mm_list[index] = MatCi
        elif value == "MatDi":
            mm_list[index] = MatDi
        else:
            mm_list.remove(value)
    try:
        resultant_matrix_mult = mm_list[0]
        for next_one in range(1, len(mm_list)):
            resultant_matrix_mult = matrix_multiplication1(resultant_matrix_mult, mm_list[next_one])
            if resultant_matrix_mult=="Dimension Error":
                break
        if resultant_matrix_mult=="Dimension Error":
            messagebox.showerror("Dimension Error", "The column of first matrix must be equal to the row of the other")
            options()
        else:
            display("Result of", "Matrix Multiplication",resultant_matrix_mult)
            Mat_ans=resultant_matrix_mult
    except IndexError:  ##if user goes on with addition without defining matrices
        messagebox.showerror("Dimension Error", "The matrix is undefined")
        options()

##5
def transposition():
    global trp
    global Mat_ans
    mat_t, name_t = user_matrix_choice1()

    trp = []
    try:
        for x in range(len(mat_t[0])):
            k=[]
            for y in range(len(mat_t)):
                k.append(mat_t[y][x])
            trp.append(k)
    except IndexError:
        messagebox.showerror("Dimension Error", "The Matrix is undefined")
    else:
        display("Transpose of",name_t,trp)
        Mat_ans=trp


##6 (i)
def determinant():
    mat_d , name_d= user_matrix_choice1()
    destroy()
    det_ans=0
    try:
        if len(mat_d)==len(mat_d[0]): ## checking whether it's a square matrix or not
            if len(mat_d)==2:
                det_ans=det_mat_2x2(mat_d)
            elif len(mat_d)>=3:
                det_ans=det_mat_gtet3(mat_d)
            Label(e_frame, text="The determinant of " + str(name_d) + " is", font=("Aerial", 10, "bold"), bg="#203873",
                  fg="white", anchor=CENTER,
                  width=25,
                  height=2).grid(row=0, column=0, padx=25, pady=50)
            Label(e_frame, text=str(det_ans), font=("Aerial", 15, "bold"), bg="#203873", fg="white", anchor=CENTER,
                  width=15,
                  height=3).grid(row=1, column=0, padx=50, pady=25)

        else:
            messagebox.showerror("Dimension Error", "For Determinant matrix must be a square matrix")
            options()
    except IndexError:
        messagebox.showerror("Dimension Error", "Matrix is undefined")
        options()


##6 (ii)
def det_mat_2x2(matd):
    det2x2=(matd[0][0]*matd[1][1])-(matd[0][1]*matd[1][0])
    return det2x2

##6 (iii)
def det_mat_gtet3(matrixd):
    ans=0
    spl_det=mat_spl(0, matrixd)
    for i in range(len(matrixd[0])):
        k= (spl_det[i]) * (matrixd[0][i])
        ans=ans+((-1)**i)*k
    return ans

##6 (iii)(a)
def mat_spl(nrpos, matrixs):
    spl_det=[]
    for ncpos in range(len(matrixs[0])):
        s1 = []
        for i in range(len(matrixs)):
            r1 = []
            if i != nrpos:
                for j in range(len(matrixs[0])):
                    if j != ncpos:
                        k = matrixs[i][j]
                        r1.append(k)

                s1.append(r1)
        if len(matrixs)==3:
            d = det_mat_2x2(s1)
            spl_det.append(d)
        elif len(matrixs)>=4:
            d= det_mat_gtet3(s1)
            spl_det.append(d)
    return spl_det

##7
def inverse():
    mat_i, name_i = user_matrix_choice1()
    inv = []
    try:
        if len(mat_i) == len(mat_i[0]):  ## checking whether it's a square matrix or not
            if len(mat_i) == 2:
                inv = inverse_mat_2x2(mat_i)
            elif len(mat_i) >= 3:
                inv = inverse_mat_gtet3(mat_i)
            display("Inverse of", name_i, inv)
        else:
            messagebox.showerror("Dimension error", "For Inverse matrix must be a square matrix")
    except ZeroDivisionError:
        messagebox.showerror("Undefined!", "Determinant is Zero")
        options()
    except IndexError:
        messagebox.showerror("Dimension Error!", "Matrix is undefined")
        options()
    else:
        global MatAi
        global MatBi
        global MatCi
        global MatDi
        global Mat_ans

        Mat_ans=inv
        if name_i == "MatA":
            MatAi = inv
        elif name_i == "MatB":
            MatBi = inv
        elif name_i == "MatC":
            MatCi = inv
        elif name_i == "MatD":
            MatDi = inv

##7 (i)
def inverse_mat_2x2(matrixi):
    det=det_mat_2x2(matrixi)
    adj=adj_mat_2x2(matrixi)

    for i in range(len(adj)):
        for j in range(len(adj[0])):
            k=adj[i][j]/det
            adj[i][j]=k

    return adj

##7 (i)(a)
def adj_mat_2x2(mata):
    mata[0][0],mata[1][1]=mata[1][1],mata[0][0]
    a=mata[0][1]
    d=mata[1][0]
    mata[0][1]=-a
    mata[1][0]=-d
    return mata

##7 (ii)
def inverse_mat_gtet3(matrixi):
    det=det_mat_gtet3(matrixi)
    cof=cof_mat(matrixi)
    adj=trp_square_mat(cof)
    try:
        for i in range(len(adj)):
            for j in range(len(adj[0])):
                k=adj[i][j]/det
                adj[i][j]=k
    except ZeroDivisionError:
        messagebox.showerror("Undefined!", "Determinant is Zero")
        options()
    else:
        return adj    ##inverse matrix

##7 (ii)(a)
def cof_mat(matc):
    cof = []
    for nrpos in range(len(matc)):
        spl_det=mat_spl(nrpos, matc)
        cof.append(spl_det)

    for i in range(len(cof)):
        for j in range(len(cof[0])):
            cof[i][j] = ((-1) ** (i + j)) * cof[i][j]

    return cof

##7 (ii)(b)
def trp_square_mat(matt):
    n = 0
    for i in range(len(matt)):
        for j in range(n, len(matt[0])):
            matt[i][j], matt[j][i] = matt[j][i], matt[i][j]
        n += 1
    return matt

##8
def cofactors():  ##calling 3 functions
    global Mat_ans
    try:
        mat_c, name_c = user_matrix_choice1()
        if len(mat_c)==len(mat_c[0]) and len(mat_c)!=2:
            cof=cof_mat(mat_c)
            display("Cofactors of", name_c, cof)
            Mat_ans=cof
        else:
            messagebox.showerror("Dimension Error", "For Cofactors matrix must be a square matrix and order greater than 2")
            options()
    except IndexError:
        messagebox.showerror("Dimension Error", "Matrix is undefined")
        options()

##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##
                                                       ##General Functions
##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##

def options():
    global e_screen
    global rc  ##so that everytime option is called, the old r/c data gets forgotten
    global entry_num_list
    global function ##for passing value to 'next function'
    global e_function
    global b_enter
    global pos
    global b_next

    pos=0
    b_enter.config(state="disabled")
    b_next.config(state="normal")

    rc=[]
    e_function=""  ##so that Matmult entries do not appear instead of numbers
    entry_num_list=[]
    destroy()
    matrix_functions = {1: "Define Matrix", 2: "Edit Matrix", 3: "Matrix Addition", 4: "Matrix Multiplication",
                        5: "Transposition", 6: "Determinant", 7: "Matrix Inverse", 8:"Cofactors"}

    for i in range(len(matrix_functions)-4):
        a=str(i+1)+ "  :  " + matrix_functions.get(i+1)
        Label(e_frame, text=a, font=("Aerial", 10, "bold"),bg="#203873", fg="white" ,anchor=W, width=20, height=2).grid(row=i, column=0, padx=1, pady=10)
    for j in range(5,len(matrix_functions)+1):
        b=str(j)+ "  :  " + matrix_functions.get(j)
        Label(e_frame, text=b, font=("Aerial", 10, "bold"),bg="#203873" ,anchor=W,fg="white", width=20, height=2).grid(row=j-5, column=1, padx=1, pady=10)

    e_screen = Entry(e_frame, width=20, font=("Aerial", 7), bg="#A3A3A3", borderwidth=3)
    e_screen.grid(row=5, column=0, pady=10, padx=5, columnspan=2)

    function="options"

def enter():
    global e_screen
    global pos
    global function
    global labels
    global entry_num_list
    global rc
    global b_next
    global b_enter

    if e_function=="define_rc" or e_function=="define_rc_edit":
        ##displaying entered row and column number in labels
        a=e_screen.get()
        try:
            if pos<2 and int(a) not in range(1,5):
                messagebox.showerror("Try again!", "Row and Column number should be between 1 and 4")

            else:
                if pos<2:  ##if else needed here so that when its about rows and col integer is accepted but when a replacing new number is entered it would accept a float number
                    rc.append(int(a))

                elif pos==2:
                    rc.append(float(a))
                e_screen.delete(0, END)
                Label(e_frame, text=str(a), font=("Aerial", 10, "bold"), anchor=CENTER, bg="#203873", fg="white", width=12,
                      height=2).grid(row=pos+1, column=1, padx=2, pady=15)
                pos+=1
                if e_function=="define_rc":
                    if pos==2:
                        b_next.config(state="normal")
                        b_enter.config(state="disabled")
                    function="to_define"
                elif e_function=="define_rc_edit" and pos==2:
                    Label(e_frame, text="Enter the new number", font=("Aerial", 10, "bold"), anchor=W,
                          bg="#203873", fg="white", width=25, height=2).grid(row=3, column=0, padx=2, pady=15)
                    e_screen.grid_configure(pady=2)
                    function="to_edit"

        except ValueError:
            messagebox.showerror("Try Again!", "You have clicked a wrong button")
            pos=0
            rc=[]  ## so that when define_rc is called again, previously entered values get deleted, otherwise new values would be messed up
            if e_function == "define_rc":
                define_rc("Number of rows", "Number of columns")
            elif e_function == "define_rc_edit":
                define_rc("Select the Row Number to Edit", "Select the Column Number to Edit")
            else:
                options()

    elif e_function=="define_matrix_display":
        try:
            entry_num_list.append(float(e_screen.get()))
            e_screen.delete(0,END)
            ##inserting entered value into the label
            for x,l in zip(entry_num_list,labels):
                l.config(text=str(x))
        except ValueError:
            messagebox.showerror("Wrong Entry", "No element has been entered")

    else:
        pass

def next_f():
    global function
    global matrices
    global l1
    global e_screen
    global pos
    try:
        if function=="options":  ##keeping same name as the function which passed it
            user_option = int(e_screen.get())
            if user_option == 1:
                define_matrix1()
            elif user_option == 2:
                user_mat_choice("Edit")
            elif user_option == 3:
                user_mat_choice_mult_add("Addition", "add")
            elif user_option == 4:
                user_mat_choice_mult_add("Multiplication", "mult")
            elif user_option == 5:
                user_mat_choice("Transposition")  ## asks for which matrix to do transposition on
            elif user_option == 6:
                user_mat_choice("Determinant")
            elif user_option == 7:
                user_mat_choice("Inverse")
            elif user_option == 8:
                user_mat_choice("Cofactors")

        elif function=="define_matrix1":
            try:
                matrix_no=int(e_screen.get())
                if matrix_no>4 or matrix_no<1:  ##to ensure that only shown available matrices are entered
                    messagebox.showerror("Error!", "RETRY!")
                    define_matrix1()

                else:
                    define_rc("Number of rows", "Number of columns")
            except ValueError:
                messagebox.showerror("Error!", "No Matrix is selected")

        elif function=="to_define":
            pos=0
            define_matrix_display()

        elif function=="to_edit":
            pos=0
            try:
                edit("to_edit")
            except TypeError:
                messagebox.showerror("Error!", "Matrix undefined")
                options()

        elif function=="define_matrix_display":
            global entry_num_list
            if len(entry_num_list) < rc[0]*rc[1]: ##error handling in advance to prevent IndexError from raising in all other functions of matrix if user would have not entered all elements/ lines saved/
                messagebox.showerror("Error", "All the elements of the matrix were not entered")
                define_matrix_display()
            elif len(entry_num_list) > rc[0] * rc[1]:
                messagebox.showerror("Error", "Additional Numbers Entered")
                define_matrix_display()
            else:
                define_matrix()
                options()

        elif function=="user_mat_choice_e":
            edit("initial")
        elif function=="user_mat_choice_d":
            determinant()
        elif function=="user_mat_choice_t":
            transposition()
        elif function=="user_mat_choice_i":
            inverse()
        elif function=="user_mat_choice_c":
            cofactors()
        elif function=="user_mat_choice_mult":
            matrix_multiplication()
        elif function == "user_mat_choice_add":
            matrix_addition()
        else:
            pass
    except TclError:
            messagebox.showerror("Error!", "Wrong Button clicked")
    except ValueError:
        messagebox.showerror("Error!", "No number entered") ##when next is clicked without entering a value to select from the options

##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##
                                                       ##Button Functions
##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##

def click(num):

    global function
    global e_function
    if function=="user_mat_choice_mult" or function=="forward_mult":
        a = e_screen.get()
        if function=="forward_mult" or e_function=="forward":
            matrices1 = {1: "MatAi", 2: "MatBi", 3: "MatCi", 4: "MatDi"}
        else:
            matrices1 = {1: "MatA", 2: "MatB", 3: "MatC", 4: "MatD"}
        try:
            new_matrix_name = matrices1[num]
            e_screen.delete(0, END)
            e_screen.insert(0, a + str(new_matrix_name) + " x  ")
        except KeyError:
            messagebox.showerror("Error!", "Incorrect Entry")


    elif function=="user_mat_choice_add" or function=="forward_add":
        a = e_screen.get()
        if function == "forward_add" or e_function=="forward":
            matrices1 = {1: "MatAi", 2: "MatBi", 3: "MatCi", 4: "MatDi"}
        else:
            matrices1 = {1: "MatA", 2: "MatB", 3: "MatC", 4: "MatD"}
        try:
            new_matrix_name = matrices1[num]
            e_screen.delete(0, END)
            e_screen.insert(0, a + str(new_matrix_name) + " +  ")
        except KeyError:
            messagebox.showerror("Error!", "Incorrect Entry")

    else:
        try:
            previous_num=e_screen.get()
            e_screen.delete(0, END)
            e_screen.insert(0, str(previous_num) + str(num))
        except TclError:  ##if numbers are clicked when there is no entry box
            messagebox.showerror("Error!", "Wrong Button clicked")
def clear():
    try:
        e_screen.delete(0, END)
    except TclError:  ##if clicked when there is no entry box
        messagebox.showerror("Error!", "Wrong Button clicked")

def delete():
    global function
    try:
        current_num=str(e_screen.get())
        if function == "user_mat_choice_add" or function == "user_mat_choice_mult" or e_function=="forward":
            if current_num[-1]=="i":
                current_num=current_num[:-1]    ##so that an extra space is not needed to balance the removal
            current_num = current_num[:-4]
        else:
            current_num=current_num[:-1]
        e_screen.delete(0, END)
        e_screen.insert(0, current_num)
    except TclError:  ##if clicked when there is no entry box
        messagebox.showerror("Error!", "Wrong Button clicked")

def negative():
    try:
        e_screen.insert(0, "-")
    except TclError:  ##if clicked when no entry box
        messagebox.showerror("Error!", "Wrong Button clicked")

def decimal():
    try:
        current_num = str(e_screen.get())
        current_num = current_num + "."
        e_screen.delete(0, END)
        e_screen.insert(0, current_num)
    except TclError:  ##if clicked when there is no entry box
        messagebox.showerror("Error!", "Wrong Button clicked")

def mat_ans():
    try:
        display("","Mat Ans",Mat_ans)
    except IndexError:
        messagebox.showerror("Error!", "Undefined")

def switch():
    global root
    global function

    if function=="":
        define_matrix1()
    else:
        answer=messagebox.askyesno("Confirm", "Are you sure you want to quit")
        if answer==1:
            root.quit()
        else:
            pass

##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##
                                            ##Widgets and Global Variables
##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##


                                                          ##Global Variables
MatA=[]
MatB=[]
MatC=[]
MatD=[]
MatAi=[]
MatBi=[]
MatCi=[]
MatDi=[]
resultant_matrix_mult=[]
resultant_matrix_add=[]
trp=[]
function=""
e_function=""
pos=0
name=""
rc=[]
labels=[]
entry_num_list=[]
Mat_ans=[]
matrices = {1: "MatA", 2: "MatB",3: "MatC", 4: "MatD"}

                                                         ## Defining widgets

##Background Image
from PIL import ImageTk, Image
import os
image1=Image.open(r"CalcBgImg.jpg")
bg_image=ImageTk.PhotoImage(image1)
pic=Label(root, image=bg_image)
pic.place(x=0,y=0)

##Frames
calc_frame=Frame(root, highlightcolor="#051f40", highlightbackground="#051f40", highlightthickness=5, bg="#203873", borderwidth=5)
but_frame=Frame(calc_frame, bg="#203873")
disp_frame=Frame(calc_frame, height=300, width=350, bg="#203873")
e_frame=LabelFrame(disp_frame, height=280, width=340, bg="#203873")

##Global Widgets
e_screen=Entry(e_frame,font=("Aerial", 7), width=30, bg="#A3A3A3", borderwidth=3)
l1=Label(e_frame)
el=Label(e_frame, text="")

##Buttons
b1=Button(but_frame, height=2, width=10, text="1", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=lambda: click(1))
b2=Button(but_frame, height=2, width=10, text="2", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=lambda: click(2))
b3=Button(but_frame, height=2, width=10, text="3", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=lambda: click(3))
b4=Button(but_frame, height=2, width=10, text="4", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=lambda: click(4))
b5=Button(but_frame, height=2, width=10, text="5", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=lambda: click(5))
b6=Button(but_frame, height=2, width=10, text="6", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=lambda: click(6))
b7=Button(but_frame, height=2, width=10, text="7", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=lambda: click(7))
b8=Button(but_frame, height=2, width=10, text="8", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=lambda: click(8))
b9=Button(but_frame, height=2, width=10, text="9", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=lambda: click(9))
b0=Button(but_frame, height=2, width=10, text="0", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=lambda: click(0))

b_enter=Button(but_frame, height=2, width=22, text="Enter", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", state="disabled", command=enter)
b_options=Button(but_frame, height=2, width=10, text="Options", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=options)
b_next=Button(but_frame, height=2, width=10, text="Next", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=next_f)
b_clear=Button(but_frame, height=2, width=10, text="AC", bg= "#F70303", borderwidth=3, activebackground="#2C5656", command=clear)
b_delete=Button(but_frame, height=2, width=10, text="Del", bg= "#F70303", borderwidth=3, activebackground="#2C5656", command=delete)

b_decimal=Button(but_frame, height=2, width=10, text="." ,bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=decimal)
b_mat_ans=Button(but_frame, height=2, width=10, text="Mat Ans", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=mat_ans)
b_negative=Button(but_frame, height=2, width=10, text="(-)", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=negative)
b_switch=Button(but_frame, height=2, width=10, text="ON/OFF", bg= "#3873a1", borderwidth=3, activebackground="#2C5656", command=switch)

## positioning widgets
calc_frame.pack(pady=60)
disp_frame.grid(row=0, column=0)
disp_frame.grid_propagate(FALSE)
but_frame.grid(row=1, column=0)
e_frame.grid(row=0, column=0, padx=3 , pady=8)
e_frame.grid_propagate(FALSE)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b_negative.grid(row=0, column=0)
b_options.grid(row=0, column=1)
b_mat_ans.grid(row=0, column=2)
b_switch.grid(row=0, column=3)

b0.grid(row=4, column=0)
b_decimal.grid(row=4, column=1)
b_enter.grid(row=4, column=2, columnspan=2)

b_clear.grid(row=1, column=3)
b_delete.grid(row=2, column=3)
b_next.grid(row=3, column=3)


root.mainloop()

##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##
                                                              ##THE END
##-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-##
