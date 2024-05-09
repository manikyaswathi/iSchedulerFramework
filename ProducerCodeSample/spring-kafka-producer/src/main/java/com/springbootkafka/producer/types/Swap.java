package com.springbootkafka.producer.types;

public class Swap {
    Float total, free, used, avail;

    public Swap(Float total, Float free, Float used, Float avail) {
        this.total = total;
        this.free = free;
        this.used = used;
        this.avail = avail;
    }

    public void setTotal(Float total) {
        this.total = total;
    }

    public void setFree(Float free) {
        this.free = free;
    }

    public void setUsed(Float used) {
        this.used = used;
    }

    public void setAvail(Float avail) {
        this.avail = avail;
    }

    public Float getTotal() {
        return this.total;
    }

    public Float getFree() {
        return this.free;
    }

    public Float getUsed() {
        return this.used;
    }

    public Float getAvail() {
        return this.avail;
    }
}
