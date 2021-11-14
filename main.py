import FirstTv


def main():
    tv = FirstTv.Tv()

    remote = {
        1: tv.on,
        2: tv.off,
        3: tv.volumeUp,
        4: tv.volumeDown,
        5: tv.channelUp,
        6: tv.channelDown,
    }

    print("\t\tWelcome to the TV simulator\n")

    again = None

    while again != "n":
        number = int(input("\t\tWhat would you like to do? (1 - 6):\n"
                            "1 - TV on\n"
                            "2 - TV off\n"
                            "3 - Volume up\n"
                            "4 - Volume down\n"
                            "5 - Channel Up\n"
                            "6 - Channel Down\n\n"
                            "I choose: "))

        remote.get(number, tv.error)()
        print(tv)
        again = FirstTv.ask("\nYou want to continue?: (y/n)")


main()
