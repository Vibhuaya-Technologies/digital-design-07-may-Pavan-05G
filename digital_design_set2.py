# Digital Design Set 2
questions = [
    "Compare one-hot and binary state encoding for FSMs in terms of speed, area, and testability.",
    "Name two common coding styles in Verilog/SystemVerilog that can inadvertently infer latches, and how to avoid them.",
    "Sketch the RTL interface signals needed for a simple AXI-Lite slave and describe the basic handshake.",
    "Explain metastability, sky-diver synchronizers, and how you’d verify safe signal transfer across clock domains.",
    "Briefly describe how scan chains are added in DFT and the impact on timing and reset strategy.",
    "How would you implement a small dual-ported RAM in RTL, with independent read and write ports?",
    "Demonstrate a Verilog `generate` block that instantiates a parameterized N-bit register array.",
    "Explain clock gating versus power gating, and how you’d insert clock enables in RTL for power savings.",
    "Describe the pseudo-LRU (PLRU) replacement algorithm in a 4-way set-associative cache and its hardware cost.",
    "Outline the structure of a barrel shifter that can rotate a 32-bit word left or right by any number of bits.",
    "What’s the role of property checking (SystemVerilog Assertions) versus simulation in a UVM flow?",
    "Summarize the key pipeline stages in a single-precision IEEE-754 floating-point adder.",
    "How do synthesis tools use UPF/CPF low-power intent to optimize gating and retention elements?",
    "Describe the basic components of a 2D mesh NoC router (input buffers, crossbar, arbitration).",
    "Explain how you’d memory-map a custom accelerator into an AMBA-AXI bus and handle interrupts in RTL.",
]

def main():
    for i, q in enumerate(questions, start=1):
        print(f"{i}. {q}")

if __name__ == '__main__':
    main()
