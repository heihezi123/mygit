package com.cource.testng.multiThread;

import org.testng.annotations.Test;

public class MuitiThreadOnnotion {
    //@Test(invocationCount = 10,threadPoolSize = 3) 3个线程同时运行，共执行10次
        @Test(invocationCount = 10, threadPoolSize = 3)
        public void test1() {
            System.out.println(1);
            System.out.printf("Thrad Id : %s%n", Thread.currentThread().getId());
        }

    }