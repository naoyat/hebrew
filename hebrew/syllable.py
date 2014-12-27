
def divide_syllable(parts):
    syllables = []

    if parts[0] == ['V+', None]:
        print 'V+'
        syllables.append( parts[0:1] )
        parts = parts[1:]

    while len(parts) > 0:
        if parts[0][1] == None:
            syllables[-1].append(parts[0])
            parts = parts[1:]
            continue

        if len(parts) == 1:
            syllables.append(parts)
            # parts = parts[1:]
            break

        if parts[0][1] == ':':
            syllables.append(parts[0:2])
            parts = parts[2:]
        else:
            if parts[1][1] == ':':
                if len(parts) == 3 and parts[2][1] == ':':
                    syllables.append(parts[0:3])
                    parts = parts[3:]
                else:
                    syllables.append(parts[0:2])
                    parts = parts[2:]
            else:
                syllables.append(parts[0:1])
                parts = parts[1:]

    return syllables
