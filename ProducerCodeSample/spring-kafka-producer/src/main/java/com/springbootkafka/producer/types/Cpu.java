package com.springbootkafka.producer.types;

public class Cpu {
    Float us, sy, ni, id, wa, hi, si, st;

    public Cpu(Float us, Float sy, Float  ni, Float  id, Float  wa, Float  hi, Float  si, Float  st) {
        this.us = us;
        this.sy = sy;
        this.ni = ni;
        this.id = id;
        this.wa = wa;
        this.hi = hi;
        this.si = si;
        this.st = st;
    }

    public void setUs(Float us) {
        this.us = us;
    }

    public void setSy(Float sy) {
        this.sy = sy;
    }

    public void setNi(Float ni) {
        this.ni = ni;
    }

    public void setId(Float id) {
        this.id = id;
    }

    public void setWa(Float wa) {
        this.wa = wa;
    }

    public void setHi(Float hi) {
        this.hi = hi;
    }

    public void setSi(Float si) {
        this.si = si;
    }

    public void setSt(Float st) {
        this.st = st;
    }

    public Float getUs() {
        return this.us;
    }

    public Float getSy() {
        return this.sy;
    }

    public Float getNi() {
        return this.ni;
    }

    public Float getId() {
        return this.id;
    }

    public Float getWa() {
        return this.wa;
    }

    public Float getHi() {
        return this.hi;
    }

    public Float getSi() {
        return this.si;
    }

    public Float getSt() {
        return this.st;
    }
}
