def adder(target):
	if target == 0:
		return 0

	if target < 0:
		return 0

	return (target * (target + 1) / 2)


if __name__ == "__main__":
	print(adder(5))
	print(adder(10))
