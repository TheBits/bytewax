import bytewax
import logging


def inp():
    for i in [0, 1, 2, 3, 4, "a"]:
        yield (0, i)


def double(x):
    return x * 2


def minus_one(x):
    return x - 1


def stringy(x):
    return f"<dance>{x}</dance>"


def peek(x):
    print(f"peekin at {x}")


ec = bytewax.Executor()
flow = ec.Dataflow(inp())
flow.map(double)
flow.map(minus_one)
flow.map(stringy)
flow.inspect(peek)


if __name__ == "__main__":
    # FORMAT = '%(levelname)s %(name)s %(asctime)-15s %(filename)s:%(lineno)d %(message)s'
    # FORMAT = '%(message)s'
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    ec.build_and_run()
