package com.springbootkafka.producer.types;

public class Memory {
    Float total, free, used, cache;

    public Memory(Float total, Float free, Float used, Float cache) {
        this.total = total;
        this.free = free;
        this.used = used;
        this.cache = cache;
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

    public void setCache(Float cache) {
        this.cache = cache;
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

    public Float getCache() {
        return this.cache;
    }
}
