class SwimmingPool:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.user = []

    def register_user(self, user_name):
        if self.current_capacity < self.max_capacity:
            self.user.append(user_name)
            self.current_capacity += 1
            print(f"{user_name} has been registered. Current capacity: {self.current_capacity}/{self.max_capacity}.")
        else:
            print("The pool is at full capacity. Cannot register more users.")

    def remove_user(self, user_name):
        if user_name in self.user:
            self.user.remove(user_name)
            self.current_capacity -= 1
            print(f"{user_name} has been removed. Current capacity: {self.current_capacity}/{self.max_capacity}.")
        else:
            print(f"{user_name} is not in the pool.")

    def check_status(self):
        print(f"Current capacity: {self.current_capacity}/{self.max_capacity}.")
        print(f"Users in the pool: {', '.join(self.user) if self.user else 'The pool is currently empty.'}")


def main():
    pool = SwimmingPool(max_capacity=7)

    while pool.current_capacity < pool.max_capacity:
        print("\nChoose an option:")
        print("1. Register a user")
        print("2. Remove a user")
        print("3. Check pool status")
        print("4. Exit")

        option = input("Enter your choice (1-4): ")

        if option == "1":
            user_name = input("Enter the user's name to register: ")
            pool.register_user(user_name)

        elif option == "2":
            user_name = input("Enter the user's name to remove: ")
            pool.remove_user(user_name)

        elif option == "3":
            pool.check_status()

        elif option == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose a valid number.")

    if pool.current_capacity == pool.max_capacity:
        print("\nThe pool has reached its full capacity. No more users can be registered.")
        pool.check_status()


if __name__ == "__main__":
    main()
