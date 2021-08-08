from abc import ABC, abstractmethod


class IMotorcycle(ABC):

    @abstractmethod
    def get_specs(self):
        """
        Returns motorcycle specifications
        """
        pass

    @abstractmethod
    def move(self):
        """Describes moving of motorcycle"""
        pass

    def turn_left(self) -> str:
        """Describes turning lef"""
        return f'Turning left'

    def turn_right(self) -> str:
        """Describes turning right"""
        return f'Turning right'

    def stop(self) -> str:
        """Describes breaking"""
        return f'Breaking...'

    @abstractmethod
    def refill(self):
        """Describes refilling of motorcycle"""
        pass

