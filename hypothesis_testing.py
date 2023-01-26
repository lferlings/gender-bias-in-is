import scipy.stats as stats


def test_h1(male_dict, female_dict):
    male_sorted = sorted(male_dict.items())
    female_sorted = sorted(female_dict.items())

    years, males = zip(*male_sorted)
    years, females = zip(*female_sorted)

    t, p = stats.ttest_ind(males, females)

    print()
    print("H1:")
    print("\tt =", t)
    print("\tp =", p)


def test_h2(female_dict):

    female_sorted = sorted(female_dict.items())
    years, female = zip(*female_sorted)

    years = years[1:]
    female_absolute_change = [(y - female[i - 1]) for i, y in enumerate(female)][1:]

    # Calculate the linear regression line (i.e. the best fit line) for the changes (average slope)
    slope, intercept, r_value, p_value, std_err = stats.linregress(years, female_absolute_change)

    n = len(years)
    k = 1

    f = (r_value ** 2 / (1 - r_value ** 2)) * ((n - k - 1) / k)
    p = stats.f.sf(f, k, n - k - 1)

    print()
    print("H2:")
    print("\tf =", f)
    print("\tp =", p)
    print("\tDer Anteil weiblicher Autoren steigt mit einer Steigung von", slope, "% pro Jahr. Intercept:", intercept)


def test_h3(male_dict, female_dict):
    sum = {}
    for year in male_dict.keys():
        sum[year] = male_dict[year] + female_dict[year]

    sum_sorted = sorted(sum.items())
    years, sums = zip(*sum_sorted)

    slope, intercept, r_value, p_value, std_err = stats.linregress(years, sums)

    n = len(years)
    k = 1

    f = (r_value ** 2 / (1 - r_value ** 2)) * ((n - k - 1) / k)
    p = stats.f.sf(f, k, n - k - 1)

    print()
    print("H3:")
    print("\tf =", f)
    print("\tp =", p)
    print("\tDie Anzahl Paper steigt mit einer Steigung von", slope, "pro Jahr.")


def test_h4(male_citation_dict, female_citation_dict):

    male_sorted = sorted(male_citation_dict.items())
    female_sorted = sorted(female_citation_dict.items())

    years, males = zip(*male_sorted)
    years, females = zip(*female_sorted)

    t, p1 = stats.ttest_ind(males, females)
    f, p = stats.f_oneway(males, females)

    print()
    print("H4:")
    print("\tt =", t)
    print("\tp1 =", p1)
    print("\tf =", f)
    print("\tp =", p)

