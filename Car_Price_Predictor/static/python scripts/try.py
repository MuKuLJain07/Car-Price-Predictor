def print_colored_text(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
    }
    end_color = '\033[0m'
    
    if color.lower() not in colors:
        print("Invalid color")
        return
    
    colored_text = f"{colors[color.lower()]}{text}{end_color}"
    print(colored_text)

# Example usage:
print_colored_text("Red text", "red")
print_colored_text("Green text", "green")
print_colored_text("Yellow text", "yellow")
print_colored_text("Blue text", "blue")
print_colored_text("Magenta text", "magenta")
print_colored_text("Cyan text", "cyan")
