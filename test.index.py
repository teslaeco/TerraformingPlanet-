<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Chess</title>
    <style>
        .board {
            display: grid;
            grid-template-columns: repeat(8, 50px);
            grid-template-rows: repeat(8, 50px);
            gap: 1px;
            position: relative;
        }
        .cell {
            width: 50px;
            height: 50px;
            background-color: lightgray;
            position: relative;
        }
        .cell:nth-child(even) {
            background-color: darkgray;
        }
        .highlight {
            background-color: rgba(0, 255, 0, 0.3); /* Zielony, półprzezroczysty */
        }
        .piece {
            position: absolute;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 30px;
        }
    </style>
</head>
<body>
    <div id="chess-container"></div>

    <script>
        const LAYERS = 8;
        const BOARD_SIZE = 8;

        // Tworzenie planszy
        function createBoard() {
            const container = document.getElementById('chess-container');
            for (let layer = 0; layer < LAYERS; layer++) {
                const board = document.createElement('div');
                board.classList.add('board');
                board.dataset.layer = String.fromCharCode(97 + layer); // a-h

                for (let y = 0; y < BOARD_SIZE; y++) {
                    for (let x = 0; x < BOARD_SIZE; x++) {
                        const cell = document.createElement('div');
                        cell.classList.add('cell');
                        cell.dataset.position = `${board.dataset.layer}${x},${y}`;
                        board.appendChild(cell);
                    }
                }
                container.appendChild(board);
            }
        }

        // Umieszczanie figur
        function placePieces() {
            const pieces = [
                { type: 'P', color: 'white', layer: 'a', positions: [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]] },  // piony białe
                { type: 'P', color: 'black', layer: 'h', positions: [[0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6]] },  // piony czarne
                // Dodaj inne figury (króle, hetmany itd.)
            ];

            pieces.forEach(piece => {
                piece.positions.forEach(position => {
                    const [x, y] = position;
                    const cell = document.querySelector(`.cell[data-position="${piece.layer}${x},${y}"]`);
                    if (cell) {
                        const pieceElement = document.createElement('div');
                        pieceElement.classList.add('piece');
                        pieceElement.textContent = piece.color === 'white' ? '♙' : '♟';
                        cell.appendChild(pieceElement);
                    }
                });
            });
        }

        // Podświetlanie możliwych ruchów
        function highlightMoves(x, y, layer) {
            const possibleMoves = [
                [x + 1, y],
                [x - 1, y],
                [x, y + 1],
                [x, y - 1],
                // Dodaj inne reguły ruchów
            ];

            possibleMoves.forEach(([newX, newY]) => {
                const cell = document.querySelector(`.cell[data-position="${layer}${newX},${newY}"]`);
                if (cell) {
                    cell.classList.add('highlight');
                }
            });
        }

        createBoard();
        placePieces();
        highlightMoves(1, 1, 'a');  // Podświetlenie ruchów z pozycji (1,1) na warstwie 'a'

    </script>
</body>
</html>