def isnumber(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

def calculate_meandiff_nrooterr():
    y = input ("Nhập giá trị của y: ")
    if not isnumber(y):
        print("Phải nhập số")
        return

    y_hat = input ("Nhập giá trị của y_hat: ")
    if not isnumber(y_hat):
        print("Phải nhập số")
        return

    n = input ("Nhập căn bậc n: ")
    if not n.isnumeric():
        print("Phải nhập số int")
        return

    p = input ("Nhập bậc của hàm loss: ")
    if not p.isnumeric():
        print("Phải nhập số int")
        return

    y = float(y)
    y_hat = float(y_hat)
    n = int(n)
    p = int(p)

    md_ner = (y**(1/n) - y_hat**(1/n))**p

    print(f"Mean different n root error (y={y}, y_hat={y_hat}, n={n}, p={p}) >> {md_ner}")

calculate_meandiff_nrooterr()