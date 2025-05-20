import asyncio
from functools import wraps

# A decorator to log function calls asynchronously
def async_logger(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}...")
        result = await func(*args, **kwargs)
        print(f"[LOG] {func.__name__} finished.")
        return result
    return wrapper

# A metaclass that automatically adds a hello method
class HelloMeta(type):
    def __new__(cls, name, bases, attrs):
        async def say_hello(self):
            await asyncio.sleep(0.5)  # simulate async work
            print(self.message)
        attrs['say_hello'] = say_hello
        return super().__new__(cls, name, bases, attrs)

# The main class using the metaclass
class HelloWorld(metaclass=HelloMeta):
    def __init__(self, message="Hello, World!"):
        self.message = message

    @async_logger
    async def greet(self):
        await self.say_hello()

# The main async entrypoint
async def main():
    hw = HelloWorld()
    await hw.greet()

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
