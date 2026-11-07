# 8-семинар: Хэмминг кодын құру, қатені синдром арқылы табу және түзету. 9-семинар: біркелкі код үшін 2^k >= N шарты бойынша бит санын табу, Фано шартын тексеру және префикстік кодпен хабарды декодтау.


def hamming_encode(data):
    m = len(data)
    r = 0
    while 2 ** r < m + r + 1:
        r = r + 1
    total = m + r

    powers = []
    x = 1
    while x <= total:
        powers.append(x)
        x = x * 2

    bits = []
    d = 0
    for i in range(1, total + 1):
        if i in powers:
            bits.append(0)
        else:
            bits.append(int(data[d]))
            d = d + 1

    for p in powers:
        ones = 0
        for i in range(1, total + 1):
            if i != p and (i // p) % 2 == 1:
                ones = ones + bits[i - 1]
        bits[p - 1] = ones % 2
        print("  " + str(p) + "-baqylau razriady: birlikter sany =", ones, "->", ones % 2)

    return bits, powers


def hamming_check(bits, powers):
    error = 0
    line = ""
    for p in powers:
        ones = 0
        for i in range(1, len(bits) + 1):
            if (i // p) % 2 == 1:
                ones = ones + bits[i - 1]
        e = ones % 2
        print("  tekseru", p, ":", e)
        line = str(e) + line
        if e == 1:
            error = error + p
    print("  Sindrom (ekilik):", line, " ondyq:", error)
    return error


def to_str(bits):
    s = ""
    for b in bits:
        s = s + str(b)
    return s


def part_hamming():
    data = input("Aqparattyq bitter: ")
    bits, powers = hamming_encode(data)
    print("Hemming kody C:", to_str(bits))

    pos = int(input("Burmalangan razriad nomiri: "))
    bits[pos - 1] = 1 - bits[pos - 1]
    print("Qabyldangan C*:", to_str(bits))

    error = hamming_check(bits, powers)
    if error > 0:
        bits[error - 1] = 1 - bits[error - 1]
        print("Qate", error, "-razriadta. Tuzetilgen kod:", to_str(bits))
    else:
        print("Qate tabylmady.")


def part_prefix():
    count = int(input("Alfavit quaty N: "))
    k = 0
    power = 1
    while power < count:
        power = power * 2
        k = k + 1
    print("Birkelki kod ushin", k, "bit qajet (2^" + str(k) + " = " + str(power) + ")")

    letters = ["A", "B", "C", "D"]
    codes = ["0", "10", "110", "111"]

    fano = True
    for i in range(len(codes)):
        for j in range(len(codes)):
            if i != j and codes[j][:len(codes[i])] == codes[i]:
                fano = False
    print("Fano sharty:", "oryndalady" if fano else "oryndalmaidy")

    text = input("Ekilik habar: ")
    answer = []
    word = ""
    for ch in text:
        word = word + ch
        for i in range(len(codes)):
            if word == codes[i]:
                answer.append(letters[i])
                print("  " + word + " -> " + letters[i])
                word = ""
                break
    if word != "":
        print("  Artyq bitter qaldy:", word)
    print("Natije:", "".join(answer))


while True:
    print("\n1 - Hemming kody (8-seminar)")
    print("2 - Prefikstik kod (9-seminar)")
    print("0 - Shygu")
    choice = input("Tandau: ")
    if choice == "1":
        part_hamming()
    elif choice == "2":
        part_prefix()
    elif choice == "0":
        break
    else:
        print("Durys emes tandau!")
