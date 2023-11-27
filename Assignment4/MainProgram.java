package Assignment4;
import java.util.Scanner;

class MainProgram {
    public static void main(String[] args){
        boolean hasQuit = false;
        FleetOfCars fleet = new FleetOfCars();
        Scanner input = new Scanner(System.in);

        while(!hasQuit) {      
            System.out.println("Enter option from list below:");
            System.out.println("    1) Display complete directory");
            System.out.println("    2) Enter new Car");
            System.out.println("    3) Search for Car");
            System.out.println("    4) Modify Car information");
            System.out.println("    5) Delete a record");
            System.out.println("    Q) Quit");
            System.out.print("Enter your option: ");

            String userChoice = input.nextLine();

            if(userChoice.equals("1")) { // Display complete directory
                System.out.print(fleet);
                continue;
            }

            if(userChoice.equals("2")) { // Enter new Car
                try {
                    System.out.print("Enter the car's make and model: ");
                    String makeAndModel = input.nextLine();

                    System.out.print("Enter the maximum number of passengers in the car: ");
                    int maxNumOfPassengers = input.nextInt();
                    input.nextLine(); // Consume left-over newline

                    System.out.print("Enter the number of doors the car has: ");
                    int numDoors = input.nextInt();
                    input.nextLine(); // Consume left-over newline

                    Car newCar = new Car(makeAndModel, maxNumOfPassengers, numDoors);
                    fleet.add(newCar);

                    System.out.println("Successfully added the car!\n");
                    continue;

                } catch (Exception e) {
                    System.out.println("Something went wrong, try again.\n");
                    input.nextLine(); // Catch the invalid input tokens
                    continue;
                }
            }

            if(userChoice.equals("3")) { // Search for car
                System.out.print("Enter the make and model to search for: ");
                String makeModelSearch = input.nextLine();

                FleetOfCars matchedCars = fleet.search(makeModelSearch);
                if(matchedCars.getSize() == 0) {
                    System.out.println("No cars found, try again.");
                    continue;
                }
                System.out.println(matchedCars);
            }

            if(userChoice.equals("4")) { // Modify car
                System.out.print("Enter the make and model to modify: ");
                String makeModelSearch = input.nextLine();

                FleetOfCars matchedCars = fleet.search(makeModelSearch);
                if(matchedCars.getSize() == 0) {
                    System.out.println("No cars found, try again.");
                    continue;
                }

                for(int i = 0; i < matchedCars.getSize(); i++) {
                    System.out.println(matchedCars.get(i));
                    System.out.print("Would you like to modify this record? (y/n): ");

                    String userYesNo = input.nextLine();

                    if (userYesNo.toLowerCase().equals("Y") || userYesNo.toLowerCase().equals("y")) {
                        Car carToModify = matchedCars.get(i);
                        
                        System.out.print("Enter the car's make and model: ");
                        String makeAndModel = input.nextLine();
                        carToModify.setMakeAndModel(makeAndModel);

                        System.out.print("Enter the maximum number of passengers in the car: ");
                        int maxNumOfPassengers = input.nextInt();
                        input.nextLine(); // Consume left-over newline
                        carToModify.setMaximumNumberOfPassengers(maxNumOfPassengers);

                        System.out.print("Enter the number of doors the car has: ");
                        int numDoors = input.nextInt();
                        input.nextLine(); // Consume left-over newline
                        carToModify.setNumberOfDoors(numDoors);

                        System.out.println("Updated record.");
                        continue;
                    } else {
                        continue;
                    }
                }
            }

            if(userChoice.equals("5")) { // Delete record
                System.out.print("Enter the index of the record to delete: ");

                try {
                    int index = input.nextInt();
                    input.nextLine(); // Consume left-over newline
                    if(index > fleet.getSize() - 1) {
                        System.out.println("Invalid index, try again.");
                        continue;
                    }
        
                    System.out.println(fleet.get(index));
                    System.out.print("Would you like to delete this record? (y/n): ");

                    String userYesNo = input.nextLine();

                    if (userYesNo.toLowerCase().equals("Y") || userYesNo.toLowerCase().equals("y")) {
                        fleet.delete(index);
                        System.out.println("Deleted record.");
                        continue;
                    } else {
                        System.out.println("Cancelled, did not delete record.");
                        continue;
                    }
                } catch (Exception e) {
                    System.out.println("Invalid selection, please try again.\n");
                    input.nextLine(); // Catch the invalid input tokens
                    continue;
                }
            }

            if(userChoice.toLowerCase().equals("q")) { // Quit the program
                hasQuit = true;
                continue;
            }       
        }

        input.close(); // Close Scanner input to avoid mem leak
    }
}

