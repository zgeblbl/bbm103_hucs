# Student Name: Özge Bülbül
# Student ID: 2220765008
# OS module is imported to get the current directories for reading and writing the files.
import os


current_dir_path = os.getcwd()
reading_file_name = "doctors_aid_inputs.txt"  # The name of the file to read the inputs from.
reading_file_path = os.path.join(current_dir_path, reading_file_name)
writing_file_name = "doctors_aid_outputs.txt"  # The name of the file to write the outputs to.
writing_file_path = os.path.join(current_dir_path, writing_file_name)

patient_list = []  # The list that holds all the data of each patient.


# This is the 'saving to the output file' function. When called, it writes the output variable to the output file.
def save_output(output):
    with open(writing_file_path, 'a') as f:
        f.write(output)


# This is the 'create a new patient' function. When called, it adds the new patient data to the patient list.
def patient_create(x):
    row = x.split()  # Splits the row into a set of words.
    for i in range(len(row)):
        row[i] = row[i].strip(',')  # Removes the commas.
    for patient in patient_list:  # If the patient's name is already in the patient list, it writes "Patient x cannot be recorded due to duplication.".
        if row[1] in patient:
            save_output("Patient {} cannot be recorded due to duplication.\n".format(row[1]))
            return  # Ends the function and doesn't add the patient ,who is already in the list, to the list again.
    row[3:5] = [' '.join(row[3:5])]  # Unites the two words of the disease name.
    for i in range(len(row) - 1):  # Unites the treatment name words 'Targeted' and 'Therapy' to fix a problem.
        if row[i] == 'Targeted':
            row[i:i + 2] = [' '.join(row[i:i + 2])]
    row[2] = "{:.2%}".format(float(row[2]))  # Makes the diagnosis accuracy a percentage.
    row[6] = "{:.0%}".format(float(row[6]))  # Makes the treatment risk a percentage.
    patient_list.append(row[1:])  # Adds the patient's data to the patient list.
    save_output("Patient {} is recorded.\n".format(row[1]))  # Writes "Patient x is recorded".


# This is the 'remove a patient' function. When called, it removes the existing patient data from the patient list.
def patient_remove(y):
    row = y.split()  # Splits the row into a set of words.
    counter = 0
    for i in range(len(row)):
        row[i] = row[i].strip(',')  # Removes the commas.
    for patient in patient_list:
        if row[1] in patient:  # If the patient is in the list, it writes "Patient x is removed." and then removes the patient.
            save_output("Patient {} is removed.\n".format(row[1]))
            patient_list.remove(patient)
            break
        else:  # If the patient is not in the list, counter's value would be equal to the length of patient_list. Which means the patient is not in the list.
            counter = counter + 1
        if counter == len(patient_list):
            save_output("Patient {} cannot be removed due to absence.\n".format(row[1]))


reco = 0
probability_number = None


# This is the 'probability' function. When called, it calculates patient's disease probability and writes it.
def probability(z):
    lines = z.split()
    for i in range(len(lines)):
        lines[i] = lines[i].strip(',')
    for pat in range(len(patient_list)):
        if patient_list[pat][0] == lines[1]:  # Checks if the patient is in the list.
            disease = patient_list[pat][2]  # Assigned the disease variable to use later.
            accuracy = patient_list[pat][1]  # Assigned the accuracy variable to use later.
            incidence = patient_list[pat][3]  # Assigned the incidence variable to use later.
            accuracy = round(float(accuracy.strip('%')), 4)  # "%" symbol is deleted from accuracy, its value is made into float and rounded.
            a = round(1 - (accuracy / 100), 4)  # Accuracy is divided by 100, subtracted from 1 then rounded and assigned to "a".
            b = incidence.split('/')  # Incidence is split into two parts by the symbol "/" and assigned to "b".
            b = float(b[0]) / float(b[1])  # First member of b is divided by the second member and assigned to "b".
            sum = a + float(b)  # The sum of a and b are calculated and equalized to "sum".
            prob = float(b) / sum  # b is divided by sum to find the probability, and we assign it to "prob".
            if float(prob * 100) == int(prob*100):  # This part it for making the probability an integer if the decimals are zero.
                prob = "{: .0%}".format(float(prob))
            else:
                prob = "{: .2%}".format(float(prob))  # Probability is transformed to percentage.
            global probability_number  # probability_number is made global to use in the recommendation function.
            probability_number = prob.strip('%')  # We delete the "%" symbol from prob and assign it to probability_number.
            global reco  # reco is made global to use in the recommendation function.
            if reco == 1:  # Breaks if reco is 1 to not write the probability when recommendation is called.
                break
            else:
                save_output("Patient {} has a probability of{} of having {}.\n".format(lines[1], prob, disease))
                break
    else:
        save_output("Probability for {} cannot be calculated due to absence.\n".format(lines[1]))


# This is the 'recommendation' function. When called, it compares patient's disease probability and treatment risk and makes a suggestion.
def recommendation(r):
    row = r.split()
    for i in range(len(row)):
        row[i] = row[i].strip(',')
    counter = 0  # counter is used here for the same reason as in the patient_remove function.
    for pat in range(len(patient_list)):
        if patient_list[pat][0] == row[1]:
            risk = (patient_list[pat][5]).strip('%')
            global reco
            reco = 1  # reco is assigned to 1 to break the for cycle in the probability function.
            probability(r)  # probability function is called to calculate the disease probability.
            if float(probability_number) > float(risk):  # If probability is greater than risk, system suggests the treatment. If not, it doesn't suggest.
                save_output("System suggests {} to have the treatment.\n".format(row[1]))
                reco = 0  # reco is assigned to 0 to neutralize the code.
            else:
                save_output("System suggests {} NOT to have the treatment.\n".format(row[1]))
                reco = 0  # reco is assigned to 0 to neutralize the code.
        else:
            counter = counter + 1
    if counter == len(patient_list):
        save_output("Recommendation for {} cannot be calculated due to absence.\n".format(row[1]))


# This is the 'listing' function. When called, it makes a table of the patients' data in the list.
# It makes exceptions for words that are too long or too short.
def make_list():
    save_output("Patient\t""Diagnosis\t""Disease \t\t""Disease \t""Treatment\t\t""Treatment\n"
                "Name\t""Accuracy\t""Name\t\t\t""Incidence\t""Name\t\t\t""Risk\n"
                "-------------------------------------------------------------------------\n")
    for patient in patient_list:
        for i in range(len(patient)):
            patient[i] = patient[i].strip(',')
        if patient[4] == 'Surgery':
            save_output("{}\t{}\t\t{} \t{}\t{} \t\t{}\n".
                        format(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5]))
        elif patient[2] == 'Lung Cancer':
            save_output("{}\t{}\t\t{} \t{}\t{}\t{}\n".
                        format(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5]))
        elif patient[4] == 'Targeted Therapy':
            save_output("{}\t{}\t\t{}\t{}\t{}{}\n".
                        format(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5]))
        elif patient[0] == 'Su':
            save_output("{}\t\t{}\t\t{}\t{}\t{}\t{}\n".
                        format(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5]))
        else:
            save_output("{}\t{}\t\t{}\t{}\t{}\t{}\n".
                        format(patient[0], patient[1], patient[2], patient[3], patient[4], patient[5]))


# This is the 'reading inputs' function. It reads the commands and calls the required functions.
def read_input():
    with open(reading_file_path, 'r') as reading:
        for n in reading:
            if n.startswith("create "):
                patient_create(n)
            if n.startswith("remove "):
                patient_remove(n)
            if n.startswith("probability "):
                probability(n)
            if n.startswith("recommendation "):
                recommendation(n)
            if n.startswith("list"):
                make_list()


read_input()
