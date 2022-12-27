from matplotlib import pyplot as plt
import numpy as np

path = "C:/Users/lenna/sciebo/Semester 7/Fairness und Diskriminierung/essay/figures/"


def plot_males_and_females(male_dict, female_dict):
    male_sorted = sorted(male_dict.items())
    female_sorted = sorted(female_dict.items())

    years, males = zip(*male_sorted)
    years, females = zip(*female_sorted)

    plt.plot(years, males, label="männliche Autoren")
    plt.plot(years, females, label="weibliche Autoren")

    # plt.suptitle("Anzahl der Publikationen nach Geschlecht des Erstautors")
    plt.xlabel("Jahr")
    plt.ylabel("Publikationen")
    plt.legend()
    plt.savefig(path + "publications_gender.jpg")
    plt.show()


def plot_males_and_females_share(male_dict, female_dict):

    for year in male_dict.keys():
        all = male_dict[year] + female_dict[year]
        male_dict[year] = male_dict[year] * 100 / all
        female_dict[year] = female_dict[year] * 100 / all

    male_sorted = sorted(male_dict.items())
    female_sorted = sorted(female_dict.items())

    years, male = zip(*male_sorted)
    years, female = zip(*female_sorted)

    # Calculate the relative change in percentage of male authors over time
    male_percentage_change = [((y - male[i - 1]) / male[i - 1]) * 100 for i, y in enumerate(male)][:]
    female_percentage_change = [((y - female[i - 1]) / female[i - 1]) * 100 for i, y in enumerate(female)][:]

    # Calculate the linear regression line (i.e. the best fit line) for the changes (average slope)
    female_poly_coef = np.polyfit(years, female_percentage_change, 1)
    female_poly_fit = np.poly1d(female_poly_coef)

    male_poly_coef = np.polyfit(years, male_percentage_change, 1)
    male_poly_fit = np.poly1d(male_poly_coef)

    plt.plot(years, male, label="männliche Autoren")
    plt.plot(years, female, label="weibliche Autoren")
    # plt.suptitle("Anteil männliches/weibliches Geschlecht des Erstautors")
    plt.xlabel("Jahr")
    plt.ylabel("Anteil in Prozent")
    plt.legend()
    plt.savefig(path + "gender_change1.jpg")
    plt.show()

    plt.plot(years, male_percentage_change, label="Veränderung männlich")
    plt.plot(years, female_percentage_change, label="Veränderung weiblich")
    plt.plot(years, male_poly_fit(years), label="Durchschnittliche Steigung (m)")
    plt.plot(years, female_poly_fit(years), label="Durchschnittliche Steigung (w)")
    # plt.suptitle("Veränderung im Geschlechteranteil und durchschnittliche Steigung")

    plt.xlabel("Jahr")
    plt.ylabel("Prozent")
    plt.legend(loc='upper left', bbox_to_anchor=(0.5, 1.05))
    plt.savefig(path + "gender_change2.jpg")

    plt.show()


def plot_citations(male_citations, female_citations):
    male_sorted = sorted(male_citations.items())
    female_sorted = sorted(female_citations.items())

    years, males = zip(*male_sorted)
    years, females = zip(*female_sorted)

    plt.plot(years, males, label="männliche Autoren")
    plt.plot(years, females, label="weibliche Autoren")

    # plt.suptitle("Durchschnittliche Zitationen pro Publikation nach Geschlecht des Erstautors")
    plt.xlabel("Jahr")
    plt.ylabel("Zitationen pro Publikation")
    plt.legend()
    plt.savefig(path + "citations.jpg")

    plt.show()


def plot_sum(male_dict, female_dict):
    sum = {}
    for year in male_dict.keys():
        sum[year] = male_dict[year] + female_dict[year]

    sum_sorted = sorted(sum.items())
    years, sums = zip(*sum_sorted)

    plt.plot(years, sums)
    plt.show()
