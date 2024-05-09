package com.springbootkafka.producer.types;

/**
 * Example of what a utilization message could look like
 */
public class UtilizationMessage {
    Memory memory;
    Cpu cpu;
    Swap swap;
    String jobId;

    public UtilizationMessage(Memory memory, Cpu cpu, Swap swap, String jobId) {
        this.cpu = cpu;
        this.memory = memory;
        this.swap = swap;
        this.jobId = jobId;
    }

    public void setMemory(Memory memory) {
        this.memory = memory;
    }

    public void setCpu(Cpu cpu) {
        this.cpu = cpu;
    }

    public void setSwap(Swap swap) {
        this.swap = swap;
    }

    public void setjobId(String jobId) {
        this.jobId = jobId;
    }

    public Memory getMemory() {
        return this.memory;
    }

    public Cpu getCpu() {
        return this.cpu;
    }

    public Swap getSwap() {
        return this.swap;
    }

    public String getjobId() {
        return this.jobId;
    }
}
