def list_roman_emperors(*args, **kwargs):
    succeeded_emperors= {}
    failed_emperors = {}
    for emperor, success in args:
        if success:
            succeeded_emperors[emperor] = kwargs[emperor]
        else:
            failed_emperors[emperor] = kwargs[emperor]
    succeeded_emperors = dict(sorted(succeeded_emperors.items(), key=lambda item: (-item[1], item[0]))) #-item[1] sorts in descending order item[0] sorts alphabetically if they have the same length
    failed_emperors = dict(sorted(failed_emperors.items(), key=lambda item: (item[1], item[0])))

    result_succeeded = [f"****{name}: {ruled}" for name, ruled in succeeded_emperors.items()]
    result_failed = [f"****{name}: {ruled}" for name, ruled in failed_emperors.items()]

    emperors_count = len(succeeded_emperors) + len(failed_emperors)
    output = f"Total number of emperors: {emperors_count}\n"

    if any(succeeded_emperors):
        output += "Successful emperors:\n" + "\n".join(result_succeeded)
    if any(failed_emperors):
        output += "\nUnsuccessful emperors:\n" + "\n".join(result_failed)

    return output


print(list_roman_emperors(("Augustus", True), ("Nero", False),
                          Augustus=40, Nero=14,))


print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True),
                          Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))