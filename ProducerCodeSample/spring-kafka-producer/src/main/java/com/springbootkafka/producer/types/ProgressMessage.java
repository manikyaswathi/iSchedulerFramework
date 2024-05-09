package com.springbootkafka.producer.types;

/**
 * An example of what a progress message could look like
 */
public class ProgressMessage {
    private long epochsCompleted, totalEpochs;
    private int days, hours, minutes;
    private String jobId;
    
    public ProgressMessage(long epochsCompleted, long totalEpochs, int days, int hours, int minutes, String jobId) {
        this.epochsCompleted = epochsCompleted;
        this.totalEpochs = totalEpochs;
        this.days = days;
        this.hours = hours;
        this.minutes = minutes;
        this.jobId = jobId;
    }

    public void setEpochsCompleted(long epochsCompleted) {
        this.epochsCompleted = epochsCompleted;
    }

    public void setTotalEpochs(long totalEpochs) {
        this.totalEpochs = totalEpochs;
    }

    public void setDays(int days) {
        this.days = days;
    }

    public void setHours(int hours) {
        this.hours = hours;
    }

    public void setMinutes(int minutes) {
        this.minutes = minutes;
    }

    public void setjobId(String jobId) {
        this.jobId = jobId;
    }

    public long getEpochsCompleted() {
        return this.epochsCompleted;
    }

    public long getTotalEpochs() {
        return this.totalEpochs;
    }

    public int getDays() {
        return this.days;
    }

    public int getHours() {
        return this.hours;
    }

    public int getMinutes() {
        return this.minutes;
    }

    public String getjobId() {
        return this.jobId;
    }
}
