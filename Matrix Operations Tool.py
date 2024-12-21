import numpy as np
def CreateMatrix(p):
    print(p)
    print("Please choose the matrix you want to create")
    print("1 : For Null Matix")
    print("2 : For Identity Matrix")
    print("3 : For Custom Matrix")
    choice = int(input("Enter the choice : "))
    
    if choice == 1:
        print("Size of the matrix")
        rows = int(input("Enter the size of rows : "))
        cols = int(input("Enter the size of colums : "))
        if rows <= 0 or cols <= 0:
            print("Error : Please enter the values of rows and columns more than 0.")
            return CreateMatrix()
        else:
            tempMatrix = np.zeros((rows,cols))
            return tempMatrix
    
    elif choice == 2:
        print("Size of the matrix")
        size = int(input("Enter the size of matrix : "))
        if size <= 0:
            print("Error : Please enter the value of matrix size more than 0.")
            return CreateMatrix()
        else:    
            tempMatrix = np.identity(size)
            return tempMatrix
    
    elif choice == 3:
        print("Size of the matrix")
        rows = int(input("Enter the size of rows : "))
        cols = int(input("Enter the size of colums : "))
        if rows <= 0 or cols <= 0:
            print("Error : Please enter the values of rows and columns more than 0.")
            return CreateMatrix()
        else:
            print("Enter the elements row by row (space-separated):")
            temp =[]
            for i in range(rows):
                row = list(map(float,input(f"Row {i+1} : ").split()))
                if len(row) != cols:
                    print("Error : The number of elements doesn't match the specified number of columns.")
                temp.append(row)
            tempMatrix = np.array(temp)
            return tempMatrix
    else:
        print("Error : Choice is invalid.")
        return CreateMatrix()

def Main():
    while True:
        print("Matrix Operations Tool")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")
        operation = int(input("Enter the Operation : "))

        if operation == 1:
            A = CreateMatrix("Enter the First Matrix : ")
            B = CreateMatrix("Enter the Second Matrix : ")
            if A.shape != B.shape:
                print("Error : Both Matrix must have same size for Addition.")
            else:
                print(f"Result of Addition : {A+B}")

        elif operation == 2:
            A = CreateMatrix("Enter the First Matrix : ")
            B = CreateMatrix("Enter the Second Matrix : ")
            if A.shape != B.shape:
                print("Error : Both Matrix must have same size for Subtraction.")
            else:
                print(f"Result of Subtraction : {A-B}")

        elif operation == 3:
            A = CreateMatrix("Enter the first matrix:")
            B = CreateMatrix("Enter the second matrix:")
            if A.shape[1] != B.shape[0]:
                print("Error : Number of columns of the first matrix must equal the number of rows of the second matrix.")
            else:
                print("Result of Multiplication:\n", np.dot(A, B))

        elif operation == 4:
            A = CreateMatrix("Enter the matrix:")
            print("Transpose of the Matrix:\n", A.T)

        elif operation == 5:
            A = CreateMatrix("Enter the square matrix:")
            if A.shape[0] != A.shape[1]:
                print("Error : Determinant can only be calculated for square matrices.")
            else:
                print("Determinant of the Matrix:", round(np.linalg.det(A), 2))

        elif operation == 6:
            print("Exiting the Matrix Operations Tool.")
            break        

        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    Main()