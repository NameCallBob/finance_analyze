def gen_amort_sched(amt, rate, term_yr, freq, delay=0, int_chg=None):
    total_pmts = term_yr * freq
    monthly_rate = rate / 12 / 100
    monthly_pmt = amt * (monthly_rate * (1 + monthly_rate)
                         ** total_pmts) / ((1 + monthly_rate) ** total_pmts - 1)
    sched = []
    bal = amt
    for i in range(total_pmts):
        if i < delay:
            sched.append((i + 1, 0, 0, bal))
        else:
            int_pmt = bal * monthly_rate
            if int_chg and i >= int_chg['per']:
                monthly_rate = int_chg['new_rate'] / 12 / 100
                int_pmt = bal * monthly_rate
            princ_pmt = monthly_pmt - int_pmt
            bal -= princ_pmt
            sched.append((i + 1, round(monthly_pmt, 2),
                         round(int_pmt, 2), round(princ_pmt, 2), round(bal, 2)))
    return sched


if __name__ == "__main__":
    amt = 100000 # 貸款金額
    rate = 5 # 年利率
    term_yr = 5 # 貸款期限
    freq = 6 #每年還款
    delay = 0 #延後還款
    int_chg = None
    amort_sched = gen_amort_sched(amt, rate, term_yr, freq, delay, int_chg)
    print("Pmt#\tAmt\tInt\tPrinc\tBal")
    for pmt in amort_sched:
        print("{}\t{}\t{}\t{}\t{}".format(
            pmt[0], pmt[1], pmt[2], pmt[3], pmt[4]))
