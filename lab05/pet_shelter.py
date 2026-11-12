
"""Pet shelter registration and adoption management system."""

import secrets
import sqlite3


class PetShelter:
    """Manage pet registration, adoption, and shelter statistics."""

    def __init__(self):
        """Initialize the database and adoption counter."""
        self.connection = sqlite3.connect(":memory:")
        self.adoption_count = 0

        self.connection.execute(
            """
            CREATE TABLE pets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                species TEXT,
                age INTEGER,
                adopted INTEGER
            )
            """
        )

    def register_pet(self, name, species, age, tags=None):
        """Register a pet and return its tags."""
        if tags is None:
            tags = []

        self.connection.execute(
            """
            INSERT INTO pets (name, species, age, adopted)
            VALUES (?, ?, ?, 0)
            """,
            (name, species, age),
        )

        tags.append(species)
        return tags

    def adopt(self, pet_id):
        """Mark a pet as adopted and update the adoption count."""
        cursor = self.connection.execute(
            "UPDATE pets SET adopted = 1 WHERE id = ? AND adopted = 0",
            (pet_id,),
        )

        if cursor.rowcount > 0:
            self.adoption_count += 1

    @staticmethod
    def adoption_code():
        """Generate a secure four-digit adoption code."""
        return "PET-" + str(secrets.randbelow(9000) + 1000)

    def oldest_available(self):
        """Return the name and age of the oldest available pet."""
        cursor = self.connection.execute(
            """
            SELECT name, age
            FROM pets
            WHERE adopted = 0
            ORDER BY age DESC
            LIMIT 1
            """
        )
        return cursor.fetchone()

    def clear_unadopted(self):
        """Remove all pets that have not been adopted."""
        cursor = self.connection.execute(
            "DELETE FROM pets WHERE adopted = 0"
        )
        return cursor.rowcount

    def shelter_status(self):
        """Return the current shelter activity status."""
        if self.adoption_count > 0:
            return "active"
        return "quiet"

    def close(self):
        """Close the database connection."""
        self.connection.close()


def main():
    """Run the pet shelter demonstration."""
    shelter = PetShelter()

    shelter.register_pet("Bruno", "dog", 7)
    shelter.register_pet("Mitzi", "cat", 3)
    shelter.register_pet("Kiwi", "parrot", 12)

    shelter.adopt(1)

    print(
        shelter.oldest_available(),
        shelter.adoption_code(),
        shelter.shelter_status(),
    )

    shelter.clear_unadopted()
    shelter.close()


if __name__ == "__main__":
    main()
