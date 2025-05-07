# Digital Design Set 1
questions = [
    "Explain the difference between Mealy and Moore finite-state machines and give one advantage of each.",
    "Outline how you’d build a 4-bit carry-lookahead adder using only 2-input XOR, AND, and OR gates.",
    "Show how to implement a 7:1 multiplexer using only 2:1 multiplexers in two levels.",
    "Describe the logic for an 8-input priority encoder and explain how it handles 'no asserted inputs.'",
    "What are static 1-hazards in combinational logic, and how can you eliminate them?",
    "Given a 3-to-8 decoder truth table, derive the minimal sum-of-products expression for one output.",
    "Define setup time, hold time, clock-to-Q, and explain their impact when chaining flip-flops.",
    "Design a Moore FSM that detects the pattern '1011' on a serial input stream.",
    "Compare ripple (asynchronous) and synchronous counters in terms of maximum clock frequency and glitch behavior.",
    "Explain how to implement an n-bit shift register that also supports parallel loading of data.",
    "Describe a ring counter and a Johnson counter, including their sequence lengths and decoding logic.",
    "Contrast level-sensitive latches and edge-triggered flip-flops in terms of transparency and gating.",
    "How does a 2-to-4 decoder differ from a 1-to-4 demultiplexer, and when would you use each?",
    "Outline how you’d implement a 4-bit BCD adder, handling decimal correction for sums > 9.",
    "Provide an example Boolean function that exhibits a glitch and show the extra term needed to fix it.",
]

def main():
    for i, q in enumerate(questions, start=1):
        print(f"{i}. {q}")

if __name__ == '__main__':
    main()
