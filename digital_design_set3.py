# Digital Design Set 3
questions = [
    "Design a 2-to-4 decoder with an active-high enable input using only NAND gates. Draw the gate-level schematic.",
    "Define propagation delay and contamination delay. Show how they affect a two-gate series path.",
    "Create the truth table and minimal logic for a BCD to seven-segment display decoder, exploiting don't-cares.",
    "Design a 4-bit magnitude comparator that outputs 'A > B', 'A = B', and 'A < B' using 1-bit comparators.",
    "Implement an even-parity generator and checker for an 8-bit bus, and explain single-bit error detection.",
    "Sketch the state diagram and next-state equations for a 4-bit Gray-code counter.",
    "Provide an example of a static-0 hazard in F(A,B,C) = A·B + Ā·C, and show the consensus term to fix it.",
    "Design a 4-bit synchronous up/down counter with separate UP and DOWN control inputs.",
    "Describe a two-flop synchronizer chain and how it reduces the probability of metastability failures.",
    "Show how to build a positive-edge detector using a D flip-flop and logic gates, and timing considerations.",
    "Minimize G(A,B,C,D) = Σm(1,2,5,7,8,10,13,14) with Karnaugh maps and implement with NAND logic.",
    "Convert a JK flip-flop into a T flip-flop by tying inputs; show the resulting truth table.",
    "Design a 4-bit shift register that shifts right on CLK and parallel-loads on LOAD=1; provide RTL equations.",
    "Create a one-shot pulse-stretch circuit that outputs a fixed-width pulse regardless of input pulse width.",
    "Compare overlapping (Mealy) vs non-overlapping (Moore) '1101' sequence detectors in terms of outputs and states.",
]

def main():
    for i, q in enumerate(questions, start=1):
        print(f"{i}. {q}")

if __name__ == '__main__':
    main()
