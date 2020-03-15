"""Implementation of role, where `Node` should resend received message."""
from simulation.roles import Role
from simulation.nodes import Node


class Relay(Role):

    def perform(self):
        """Start process of frame retransmission."""
        message = self.receive_message()
        self.decode_message(message)
        receiver = self.find_receiver()
        self.send_message(receiver)

    def receive_message(self) -> bytes:
        """Simulate message receiving."""
        pass

    def decode_message(self) -> 'Message':
        """Parse received message into `Frame`."""
        pass

    def find_receiver(self, message: 'Message') -> Node:
        """Looks for receiver based on message param."""
        pass

    def send_message(self, message, receiver) -> None:
        """Sends `message` to `receiver`."""
        pass
