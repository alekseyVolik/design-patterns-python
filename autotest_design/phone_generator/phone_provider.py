from autotest_design.phone_generator import singleton


@singleton.singleton
class PhoneProvider:
    """
    Provides phone numbers that respond to pattern
    """

    def __init__(self) -> None:
        self.current_pos = 0
        self.phone_pull = [f'{"+79" if num == 0 else "9"}{num:0>9}' for num in range(11)]
        self.max_size = len(self.phone_pull)

    def get_phone_number(self) -> str:
        """
        Returns phone if limit isn`t exceeded, else raise error
        :return str: phone number
        """
        if self.current_pos >= self.max_size:
            raise IndexError("Phone number: limit is exceeded")
        phone = self.phone_pull[self.current_pos]
        self.current_pos += 1
        return phone

    def resent_index(self) -> None:
        """Reset pointer, usually in end of test"""
        self.current_pos = 0
