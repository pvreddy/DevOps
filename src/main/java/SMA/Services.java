

package SMA;

import java.math.BigInteger;
import java.util.function.Consumer;
import java.util.function.Supplier;

public class Services {
    private static Services INSTANCE;

    private final Worker worker;
    private final Require require;
    private final Global global;

    Algorithms algorithms;

    public Services(Require require, Global global, Worker worker) {
        this.require = require;
        this.global = global;
        this.worker = worker;
        INSTANCE = this;
    }

    public static Services getDefault() {
        return INSTANCE;
    }

    public void postInit(Algorithms newAlgorithms) {
        if (newAlgorithms == null) {
            throw new NullPointerException();
        }
        this.algorithms = newAlgorithms;
    }

    public interface Require {
        Object require(String module);
    }

    public interface Global {
        public Interop Interop();
        public void quit();
        public Http cast(Object value, Http prototype);
        public Server cast(Object value, Server prototype);
        public Computation cast(Object value, Computation prototype);
    }

    public interface Interop {
        public Object eval(String mimeType, String code);
        public void export(String name, Object obj);
    }

    @FunctionalInterface
    public interface Worker {
        public <T> void submit(Supplier<T> background, Consumer<T> finish);
    }

    public interface Http {
        public Server createServer(Handler handler);
    }

    @FunctionalInterface
    public interface Handler {
        public void call(Object thiz, IncommingMessage in, ServerResponse out);
    }

    public interface Server {
        public void listen(int port);
    }

    public interface IncommingMessage {
        String url();
    }

    public interface ServerResponse {
        void end(String text);
    }

    public BigInteger factorial(int value) {
        BigInteger one = BigInteger.valueOf(1);
        BigInteger n = BigInteger.valueOf(value);
        BigInteger result = one;
        while (n.compareTo(one) >= 0) {
            result = result.multiply(n);
            n = n.subtract(one);
        }
        return result;
    }

    public interface Algorithms {
        BigInteger java(int n);
        Number js(int n);
    }

    @FunctionalInterface
    public interface Computation {
        public Object compute(Object value);
    }

}
