import csv
import matplotlib.pyplot as plt
import scipy.stats as stats
import statistics

path = "C:/Users/lenna/sciebo/Semester 7/Fairness und Diskriminierung/essay/figures/"

institute_path = "./data/institute_data.csv"
institute_male_share = {}
institute_female_share = {}
hyp_dict = {}
with open(institute_path, 'r') as institute_file:
    institute_data = csv.reader(institute_file)
    for row in institute_data:
        year = row[0]
        sum = int(row[1])
        male = int(row[2]) * 100 / sum
        female = int(row[3]) * 100 / sum
        institute_male_share[year] = male
        institute_female_share[year] = female

students_path = "./data/destatis/21311-0003.csv"
students_male_share = {}
students_female_share = {}
with open(students_path, 'r') as students_file:
    students_data = csv.reader(students_file, delimiter=';')
    for row in students_data:
        if len(row) == 1:
            break
        year = int('20' + row[0].split('/')[1])
        sum = int(row[11])
        male = int(row[9]) * 100 / sum
        female = int(row[10]) * 100 / sum
        hyp_dict[year] = int(row[10])
        students_male_share[year] = male
        students_female_share[year] = female


def compare_institute(male_share_dict, female_share_dict):
    male_sorted = sorted(male_share_dict.items())
    female_sorted = sorted(female_share_dict.items())

    years, male = zip(*male_sorted)
    years, female = zip(*female_sorted)
    y, inst_male = zip(*sorted(institute_male_share.items()))
    y, inst_female = zip(*sorted(institute_female_share.items()))

    # calc correlation
    r_male, p_male = stats.pearsonr(male, inst_male)
    r_female, p_female = stats.pearsonr(female, inst_female)

    print()
    print(f"Male inst: r = {r_male}; p = {p_male}")
    print(f"Female inst: r = {r_female}; p = {p_female}")
    print()

    # calc measurements of datasets
    print_stats(male, "Authors")
    print_stats(inst_male, "Institute")
    print()

    # Test significance of data deviation
    t, p = stats.ttest_ind(male, inst_male)
    print("t =", t)
    print("p =", p)
    print()
    print()


def compare_students(male_share_dict, female_share_dict):
    male_sorted = sorted(male_share_dict.items())
    female_sorted = sorted(female_share_dict.items())

    years, male = zip(*male_sorted)
    years, female = zip(*female_sorted)
    years, stu_male = zip(*sorted(students_male_share.items()))
    years, stu_female = zip(*sorted(students_female_share.items()))

    # calc correlation
    r_male, p_male = stats.pearsonr(male, stu_male)
    r_female, p_female = stats.pearsonr(female, stu_female)
    print(f"Male students: r = {r_male}; p = {p_male}")
    print(f"Female students: r = {r_female}; p = {p_female}")
    print()

    # calc measurements of datasets
    print_stats(male, "Authors")
    print_stats(stu_male, "Students")
    print()

    # Test significance of data deviation
    t, p = stats.ttest_ind(male, stu_male)
    print("t =", t)
    print("p =", p)
    print()
    print()


def compare_plots(male_share_dict, female_share_dict):
    male_sorted = sorted(male_share_dict.items())
    female_sorted = sorted(female_share_dict.items())

    years, male = zip(*male_sorted)
    _, female = zip(*female_sorted)
    _, inst_male = zip(*sorted(institute_male_share.items()))
    _, inst_female = zip(*sorted(institute_female_share.items()))
    _, stu_male = zip(*sorted(students_male_share.items()))
    _, stu_female = zip(*sorted(students_female_share.items()))

    plt.plot(years, male, label="männliche Autoren")
    plt.plot(years, female, label="weibliche Autoren")
    plt.plot(years, inst_male, label="männliche Mitarbeitende")
    plt.plot(years, inst_female, label="weibliche Mitarbeitende")
    plt.plot(years, stu_male, label="männliche Studierende")
    plt.plot(years, stu_female, label="weibliche Studierende")

    plt.xlabel("Jahr")
    plt.ylabel("Prozent")
    plt.legend()
    plt.savefig(path + "compare.jpg")
    plt.show()


def print_stats(data, flag):
    print(f"{flag}: Mean =", statistics.mean(data))
    print(f"{flag}: Median =", statistics.median(data))
    print(f"{flag}: SD =", statistics.stdev(data))
