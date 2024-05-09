package com.springbootkafka.producer.types;

/**
 * An example of what a performance message could look like
 */
public class PerformanceMessage {
    private float accuracy, fmeasure, precision, recall;
    private String jobId;
    
    public PerformanceMessage(float accuracy, float fmeasure, float precision, float recall, String jobId) {
        this.accuracy = accuracy;
        this.fmeasure = fmeasure;
        this.precision = precision;
        this.recall = recall;
        this.jobId = jobId;
    }

    public void setAccuracy(float accuracy) {
        this.accuracy = accuracy;
    }

    public void setFmeasure(float fmeasure) {
        this.fmeasure = fmeasure;
    }

    public void setPrecision(float precision) {
        this.precision = precision;
    }

    public void setRecall(float recall) {
        this.recall = recall;
    }

    public void setjobId(String jobId) {
        this.jobId = jobId;
    }

    public float getAccuracy() {
        return this.accuracy;
    }

    public float getFmeasure() {
        return this.fmeasure;
    }

    public float getPrecision() {
        return this.precision;
    }

    public float getRecall() {
        return this.recall;
    }

    public String getjobId() {
        return this.jobId;
    }
}
