def stable_marriage(num, men, women):
    m_status = {}
    w_status = {}
    for man in men:
        m_status[man] = False
    for w in women:
        w_status[w] = False
    for order in range(num):
        print("Day", order + 1)
        for woman in women:
            if w_status[woman] is False:
                if m_status[women[woman][order]] is False:
                    print(woman, "Proposes to", women[woman][order])
                    m_status[women[woman][order]] = woman
                    w_status[woman] = m_status[women[woman][order]]
                    print(women[woman][order], "Accepts")
                else:
                    print(woman, "Proposes to", women[woman][order])
                    alr_wom = men[women[woman][order]].index(
                        m_status[women[woman][order]]
                    )
                    cur_wom = men[women[woman][order]].index(woman)
                    if cur_wom < alr_wom:
                        print(
                            women[woman][order],
                            "rejects",
                            m_status[women[woman][order]],
                            "for",
                            woman,
                        )
                        for i in m_status:
                            if m_status[i] == woman:
                                m_status[i] = False
                                w_status[woman] = False
                        w_status[m_status[women[woman][order]]] = False
                        m_status[women[woman][order]] = woman
                        w_status[woman] = m_status[women[woman][order]]

        print(m_status)
    return m_status


men = {"M1": ["W2", "W3", "W1"], "M2": ["W1", "W2", "W3"], "M3": ["W2", "W1", "W3"]}
women = {"W1": ["M1", "M2", "M3"], "W2": ["M2", "M1", "M3"], "W3": ["M1", "M2", "M3"]}

results = stable_marriage(3, men, women)
for i in results:
    print(i, ":", results[i])
