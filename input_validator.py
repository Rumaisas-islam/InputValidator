class InputValidator:
  def __init__(self):
    self.ask=input("Enter your username: ")
  def checker(self):
    valid_char=self.ask.isalnum()
    banned_words=["admin","root"]
    no_banned_words=not any(word in self.ask.lower() for word in banned_words)
    banned_endings=["123","000"]
    no_banned_endings=not any(self.ask.endswith(end) for end in banned_endings)
    valid_length=len(self.ask)>=5
    if valid_char and no_banned_endings and no_banned_words and valid_length:
      print("✅ Valid Username")
    else:
      print("❌ Invalid Username")
      if not valid_char:
        print("→ Username should only contain letters and numbers (no spaces/symbols.")
      if not no_banned_endings:
        print("→Username should not end with '123' or '000'.")
      if not no_banned_words:
        print("Username should not contain 'admin' or 'root'.")
      if not valid_length:
        print("→ Username should be at least 5 characters long.")
obj=InputValidator()
obj.checker()

