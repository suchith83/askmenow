function deleteQuestion() {
    document.addEventListener('DOMContentLoaded', () => {
        const deleteButtons = document.querySelectorAll('.delete-question');
        deleteButtons.forEach(button => {
            console.log('button worked ..................');
            button.addEventListener('click', event => {
                event.preventDefault();
                const questionId = button.dataset.questionid;
                const username = button.dataset.username;
                if (confirm("Are you sure you want to delete this question?")) {
                    fetch(`/profile/${username}/questions/${questionId}`, {
                        method: 'DELETE',
                    })
                        .then(response => {
                            if (response.ok) {
                                window.location.href = `/profile/${username}/questions`;
                            }
                        })
                        .catch(error => console.error(error));
                }
            });
        });
    });

}
