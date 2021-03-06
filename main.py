def split(line, number):
    num = ["states", "alpha", "initial", "accepting", "trans"]
    if "[" not in line or "]" not in line or num[number] not in line:  # check order and file correct
        with open("output.txt", "w") as err:
            err.write("Error:\n")
            err.write("E0: Input file is malformed")
            raise SystemExit(0)

    try:
        line = line.replace("[", "")  #
        line = line.replace("]", "")  # replace elements and create array of data
        line = line.replace("\n", "")  #
        line = line.replace(num[number] + "=", "")
        line = line.split(",")
        if line[0] == '':
            line = []
        return line

    except:
        with open("output.txt", "w") as err:
            err.write("Error:\n")
            err.write("E0: Input file is malformed")
            raise SystemExit(0)


def E0(data):
    res = []
    for i in data:
        for j in i:
            res.append(j)

    if len(res) == 0:
        with open("output.txt", "w") as err:
            err.write("Error:\n")
            err.write("E0: Input file is malformed")
            raise SystemExit(0)


def E1(data):
    # check all states. They should be in array of states
    for i in data[2]:
        if i not in data[0]:
            with open("output.txt", "w") as err:
                err.write("Error:\n")
                err.write("E1: A state '" + i + "' is not in the set of states")
                raise SystemExit(0)
    for i in data[3]:
        if i not in data[0]:
            with open("output.txt", "w") as err:
                err.write("Error:\n")
                err.write("E1: A state '" + i + "' is not in the set of states")
                raise SystemExit(0)

    for i in data[-1]:
        trans_data = i.split(">")
        for j in range(0, len(trans_data), 2):
            if trans_data[j] not in data[0]:
                with open("output.txt", "w") as err:
                    err.write("Error:\n")
                    err.write("E1: A state '" + i + "' is not in the set of states")
                    raise SystemExit(0)


def E2(data):
    # check states disjoint
    states = data[0]
    trans = data[-1]
    trans2 = []

    for i in trans:
        s = i.split(">")
        s = s[0] + ">" + s[2]
        trans2.append(s)

    for i in states:
        if i not in data[2] and i not in data[3]:
            IN_TF = False
            OUT_TF = False
            for j in range(len(trans2)):
                if i + ">" in trans2[j] and trans2[j].split(">")[0] != trans2[j].split(">")[1]:
                    IN_TF = True
                if ">" + i in trans2[j] and trans2[j].split(">")[0] != trans2[j].split(">")[1]:
                    OUT_TF = True

            if not IN_TF and not OUT_TF:
                with open("output.txt", "w") as err:
                    err.write("Error:\n")
                    err.write("E2: Some states are disjoint")
                    raise SystemExit(0)


def E3(data):
    # check transitions. They should be in array of trans
    for i in data[-1]:
        trans_data = i.split(">")
        for j in range(1, len(trans_data), 2):
            if trans_data[j] not in data[1]:
                with open("output.txt", "w") as err:
                    err.write("Error:\n")
                    err.write("E3: A transition '" + trans_data[j] + "' is not represented in the alphabet")
                    raise SystemExit(0)


def E4(data):
    # check existing initial state
    if not data[2]:
        with open("output.txt", "w") as err:
            err.write("Error:\n")
            err.write("E4: Initial state is not defined")
            raise SystemExit(0)


def E5(data):
    check_trans = {}
    for i in data[0]:
        check_trans[i] = []
    trans = []
    for i in data[-1]:
        trans.append(i.split(">"))
    for i in trans:
        if i[1] not in check_trans[i[0]]:
            check_trans[i[0]].append(i[1])
        else:
            with open("output.txt", "w") as err:
                err.write("Error:\n")
                err.write("E5: FSA is nondeterministic")
                raise SystemExit(0)


def minus_one_step(i, j):
    if i == j:
        TF = False
        c = []
        for el in trans:
            if el[0] == el[-1] and el[0] == states[i]:
                TF = True
                c.append(el[1])
        if len(c) >= 1:
            wr = "("
            for l in c:
                wr += l + "|"
            wr += "eps)"
            resmas[k][i][j] = wr
        if not TF:
            resmas[k][i][j] = "(eps)"
    else:
        TF = False
        for el in trans:
            if el[0] == states[i] and el[-1] == states[j]:
                TF = True
                resmas[k][i][j] = "(%s)" % el[1]
        if not TF:
            resmas[k][i][j] = "({})"


with open("input.txt") as fsa_file:  # open file
    data = []  # array with input data
    warnings = []  # array with warnings

    j = 0
    for i in fsa_file.readlines():  # correct file or not
        data.append(split(i, j))
        j += 1
    E0(data)
    E1(data)
    E2(data)
    E3(data)
    E4(data)
    E5(data)

    states = data[0]
    if len(data[3]) == 0:
        with open("output.txt", "w") as err:
            err.write("{}")
            raise SystemExit(0)

    trans = []
    for i in data[-1]:
        trans.append(i.split(">"))
    res = ""
    resmas = []

    for k in range(len(states) + 1):
        mas_k = []
        for i in range(len(states) + 1):
            mas_i = []
            for j in range(len(states) + 1):
                mas_i.append("")
            mas_k.append(mas_i)
        resmas.append(mas_k)

    for k in range(-1, len(states)):
        for i in range(len(states)):
            for j in range(len(states)):
                if i == j:
                    if k == -1:
                        minus_one_step(i, j)
                    else:
                        wr = "(" + resmas[k - 1][i][k] + resmas[k - 1][k][k] + "*" + resmas[k - 1][k][
                            j] + "|" + \
                             resmas[k - 1][i][j] + ")"
                        resmas[k][i][j] = wr
                else:
                    if k == -1:
                        minus_one_step(i, j)
                    else:
                        wr = "(" + resmas[k - 1][i][k] + resmas[k - 1][k][k] + "*" + resmas[k - 1][k][
                            j] + "|" + \
                             resmas[k - 1][i][j] + ")"
                        resmas[k][i][j] = wr

    res = ""

    for i in range(len(states)):
        for j in range(len(states)):
            if states[i] == data[2][0] and states[j] in data[3]:
                if res:
                    res += "|" + resmas[len(states) - 1][i][j][1:-1:]
                else:
                    res = resmas[len(states) - 1][i][j][1:-1:]
with open("output.txt", "w") as err:
    err.write(res)
    raise SystemExit(0)
